"""Enforce the frozen single-writer boundary for canonical persistence."""

from __future__ import annotations

import ast
import re
from dataclasses import dataclass
from pathlib import Path

import pytest


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
PACKAGES_ROOT = REPOSITORY_ROOT / "packages" / "dctm"
CANONICAL_COMMIT = Path("packages/dctm/application/canonical_commit.py")

# Architecture names a persistence-port adapter role, but the frozen material does
# not map that singular exception to a concrete file. Add only its exact repository
# path here after that mapping is frozen; never authorize an infrastructure subtree.
PERSISTENCE_ADAPTERS: tuple[Path, ...] = ()
AUTHORIZED_WRITERS = (CANONICAL_COMMIT, *PERSISTENCE_ADAPTERS)

AUTHORITY = (
    "single-writer rule: only Canonical Commit and its specifically authorized "
    "persistence port adapter may write canonical persistence "
    "(Architecture §6.2/§9; plan.md §Project Structure; T007)"
)
_SQL_MUTATION = re.compile(r"^\s*(INSERT|UPDATE|DELETE|REPLACE)\b", re.IGNORECASE)
_EXECUTION_METHODS = {"execute", "executemany", "exec_driver_sql"}
_SQLALCHEMY_MUTATORS = {"insert", "update", "delete"}
_PERSISTENCE_RECEIVERS = {
    "connection",
    "conn",
    "session",
    "transaction",
    "tx",
    "db",
    "database",
}


@dataclass(frozen=True)
class WriteViolation:
    path: Path
    line: int
    signal: str

    def diagnostic(self) -> str:
        return f"{self.path}:{self.line}: {self.signal}; violates {AUTHORITY}"


def _canonical_path(path: Path) -> Path:
    candidate = path if path.is_absolute() else REPOSITORY_ROOT / path
    return candidate.resolve(strict=False)


def _is_authorized_writer(path: Path) -> bool:
    canonical = _canonical_path(path)
    return any(canonical == _canonical_path(allowed) for allowed in AUTHORIZED_WRITERS)


def _call_name(node: ast.expr) -> str | None:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        return node.attr
    return None


def _root_name(node: ast.expr) -> str | None:
    while isinstance(node, ast.Attribute):
        node = node.value
    return node.id if isinstance(node, ast.Name) else None


def _receiver_name(node: ast.expr) -> str | None:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        return node.attr
    return None


def _literal_text(node: ast.expr) -> str | None:
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    if (
        isinstance(node, ast.Call)
        and _call_name(node.func) == "text"
        and node.args
    ):
        return _literal_text(node.args[0])
    return None


def _table_bound_mutation(
    node: ast.expr, sqlalchemy_modules: set[str]
) -> str | None:
    """Find a table-bound mutation constructor beneath statement-builder calls."""
    if not isinstance(node, ast.Call) or not isinstance(node.func, ast.Attribute):
        return None
    if (
        node.func.attr in _SQLALCHEMY_MUTATORS
        and _root_name(node.func) not in sqlalchemy_modules
    ):
        return node.func.attr
    return _table_bound_mutation(node.func.value, sqlalchemy_modules)


class _WriteSignalVisitor(ast.NodeVisitor):
    def __init__(self) -> None:
        self.signals: list[tuple[int, str]] = []
        self.sqlalchemy_modules: set[str] = set()
        self.sqlalchemy_mutators: set[str] = set()
        self.table_bound_statements: list[dict[str, str]] = [{}]

    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
        self.table_bound_statements.append({})
        self.generic_visit(node)
        self.table_bound_statements.pop()

    visit_AsyncFunctionDef = visit_FunctionDef

    def visit_Assign(self, node: ast.Assign) -> None:
        mutation = _table_bound_mutation(node.value, self.sqlalchemy_modules)
        for target in node.targets:
            if isinstance(target, ast.Name):
                if mutation:
                    self.table_bound_statements[-1][target.id] = mutation
                else:
                    self.table_bound_statements[-1].pop(target.id, None)
        self.generic_visit(node)

    def visit_Import(self, node: ast.Import) -> None:
        for alias in node.names:
            if alias.name == "sqlalchemy":
                self.sqlalchemy_modules.add(alias.asname or alias.name)

    def visit_ImportFrom(self, node: ast.ImportFrom) -> None:
        if node.module == "sqlalchemy" or (node.module or "").startswith("sqlalchemy."):
            for alias in node.names:
                if alias.name in _SQLALCHEMY_MUTATORS:
                    self.sqlalchemy_mutators.add(alias.asname or alias.name)

    def visit_Call(self, node: ast.Call) -> None:
        name = _call_name(node.func)

        if isinstance(node.func, ast.Name) and node.func.id in self.sqlalchemy_mutators:
            self.signals.append(
                (node.lineno, f"SQLAlchemy {node.func.id}() mutation statement")
            )
        elif (
            isinstance(node.func, ast.Attribute)
            and node.func.attr in _SQLALCHEMY_MUTATORS
            and _root_name(node.func) in self.sqlalchemy_modules
        ):
            self.signals.append(
                (node.lineno, f"SQLAlchemy {node.func.attr}() mutation statement")
            )

        if name in _EXECUTION_METHODS and node.args:
            sql = _literal_text(node.args[0])
            match = _SQL_MUTATION.match(sql or "")
            if match:
                self.signals.append(
                    (node.lineno, f"direct SQL {match.group(1).upper()} via {name}()")
                )
            statement = node.args[0]
            mutation = _table_bound_mutation(statement, self.sqlalchemy_modules)
            if isinstance(statement, ast.Name):
                mutation = self.table_bound_statements[-1].get(statement.id)
            if mutation:
                self.signals.append(
                    (
                        node.lineno,
                        f"SQLAlchemy table-bound {mutation}() "
                        f"mutation via {name}()",
                    )
                )

        if isinstance(node.func, ast.Attribute) and name in {"commit", "flush"}:
            receiver = _receiver_name(node.func.value)
            if receiver and receiver.lower() in _PERSISTENCE_RECEIVERS:
                self.signals.append(
                    (node.lineno, f"persistence {receiver}.{name}() transaction write")
                )

        self.generic_visit(node)


def _write_signals(source: str) -> list[tuple[int, str]]:
    visitor = _WriteSignalVisitor()
    visitor.visit(ast.parse(source))
    return visitor.signals


def _unauthorized_writes(path: Path, source: str) -> list[WriteViolation]:
    if _is_authorized_writer(path):
        return []
    return [
        WriteViolation(path=path, line=line, signal=signal)
        for line, signal in _write_signals(source)
    ]


def _repository_violations() -> list[WriteViolation]:
    violations: list[WriteViolation] = []
    for path in sorted(PACKAGES_ROOT.rglob("*.py")):
        violations.extend(_unauthorized_writes(path, path.read_text(encoding="utf-8")))
    return violations


def _assert_no_violations(violations: list[WriteViolation]) -> None:
    assert not violations, "Unauthorized canonical persistence write(s):\n" + "\n".join(
        violation.diagnostic() for violation in violations
    )


def test_current_repository_has_no_unauthorized_persistence_writer() -> None:
    _assert_no_violations(_repository_violations())


@pytest.mark.parametrize(
    ("path", "source", "expected_signal"),
    (
        (
            Path("packages/dctm/domain/session.py"),
            'cursor.execute("INSERT INTO sessions VALUES (1)")',
            "direct SQL INSERT",
        ),
        (
            Path("packages/dctm/application/commands/activate.py"),
            "from sqlalchemy import update\nstatement = update(sessions)",
            "SQLAlchemy update()",
        ),
        (
            Path("packages/dctm/infrastructure/persistence/rogue.py"),
            "def save(connection):\n    connection.commit()",
            "persistence connection.commit()",
        ),
    ),
)
def test_rejects_unauthorized_writers(
    path: Path, source: str, expected_signal: str
) -> None:
    violations = _unauthorized_writes(path, source)

    assert len(violations) == 1
    assert violations[0].line >= 1
    assert expected_signal in violations[0].signal
    assert str(path) in violations[0].diagnostic()
    assert "single-writer rule" in violations[0].diagnostic()


@pytest.mark.parametrize(
    ("source", "expected_signal"),
    (
        (
            "connection.execute(sessions.insert())",
            "SQLAlchemy table-bound insert()",
        ),
        (
            "connection.execute(sessions.update())",
            "SQLAlchemy table-bound update()",
        ),
        (
            "connection.execute(sessions.delete())",
            "SQLAlchemy table-bound delete()",
        ),
        ("self.connection.commit()", "persistence connection.commit()"),
        ("self.transaction.commit()", "persistence transaction.commit()"),
        (
            "connection.execute(sessions.insert().values(id=1))",
            "SQLAlchemy table-bound insert()",
        ),
        (
            "connection.execute(sessions.update().where(sessions.c.id == 1))",
            "SQLAlchemy table-bound update()",
        ),
        (
            "connection.execute(sessions.delete().where(sessions.c.id == 1))",
            "SQLAlchemy table-bound delete()",
        ),
        (
            "statement = sessions.update()\nconnection.execute(statement)",
            "SQLAlchemy table-bound update()",
        ),
        (
            "statement = sessions.insert().values(id=1)\n"
            "connection.execute(statement)",
            "SQLAlchemy table-bound insert()",
        ),
    ),
)
def test_rejects_independently_verified_write_bypasses(
    source: str, expected_signal: str
) -> None:
    path = Path("packages/dctm/infrastructure/persistence/rogue.py")

    violations = _unauthorized_writes(path, source)

    assert len(violations) == 1
    assert expected_signal in violations[0].signal


def test_canonical_commit_is_the_approved_application_writer() -> None:
    source = "from sqlalchemy import insert\nstatement = insert(journal)"

    assert _write_signals(source)
    assert _unauthorized_writes(CANONICAL_COMMIT, source) == []


@pytest.mark.parametrize(
    "path",
    (
        CANONICAL_COMMIT,
        Path("packages/dctm/application/./canonical_commit.py"),
        Path("packages/dctm/domain/../application/canonical_commit.py"),
        REPOSITORY_ROOT / CANONICAL_COMMIT,
    ),
)
def test_writer_authorization_uses_canonical_repository_paths(path: Path) -> None:
    assert _is_authorized_writer(path)


def test_read_only_persistence_use_outside_writer_is_permitted() -> None:
    source = """\
from sqlalchemy import select

def load(connection, sessions):
    statement = select(sessions)
    return connection.execute(statement).fetchall()
"""

    assert _write_signals(source) == []
    assert _unauthorized_writes(
        Path("packages/dctm/infrastructure/queries.py"), source
    ) == []


def test_persistence_imports_alone_are_not_writes() -> None:
    source = "from sqlalchemy import insert, update, delete\nimport sqlcipher3"

    assert _write_signals(source) == []
    assert _unauthorized_writes(Path("packages/dctm/application/reporting.py"), source) == []
