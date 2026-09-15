"""Conformance tests for the domain package's inward dependency boundary."""

from __future__ import annotations

import ast
from dataclasses import dataclass
from pathlib import Path

import pytest


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
DOMAIN_ROOT = REPOSITORY_ROOT / "packages" / "dctm" / "domain"


@dataclass(frozen=True)
class ForbiddenDependency:
    prefix: str
    category: str
    rule: str


FORBIDDEN_DEPENDENCIES = (
    ForbiddenDependency("fastapi", "framework / WebSocket", "Architecture §9.4"),
    ForbiddenDependency("sqlalchemy", "ORM / persistence", "Architecture §9.4"),
    ForbiddenDependency("ollama", "model provider", "Architecture §9.4"),
    ForbiddenDependency("mcp", "tool provider", "Architecture §9.4"),
    ForbiddenDependency(
        "dctm.application",
        "reversed domain-to-application dependency",
        "Architecture §9.4",
    ),
    ForbiddenDependency(
        "dctm.infrastructure",
        "reversed domain-to-infrastructure dependency",
        "Architecture §9.4",
    ),
    ForbiddenDependency(
        "packages.dctm.application",
        "reversed domain-to-application dependency",
        "Architecture §9.4",
    ),
    ForbiddenDependency(
        "packages.dctm.infrastructure",
        "reversed domain-to-infrastructure dependency",
        "Architecture §9.4",
    ),
)


@dataclass(frozen=True)
class Violation:
    path: Path
    line: int
    imported_name: str
    dependency: ForbiddenDependency

    def describe(self) -> str:
        return (
            f"{self.path}:{self.line}: import {self.imported_name!r} violates "
            f"{self.dependency.rule} ({self.dependency.category}; forbidden prefix "
            f"{self.dependency.prefix!r})"
        )


def _dependency_for(imported_name: str) -> ForbiddenDependency | None:
    for dependency in FORBIDDEN_DEPENDENCIES:
        if imported_name == dependency.prefix or imported_name.startswith(
            f"{dependency.prefix}."
        ):
            return dependency
    return None


def _package_for(path: Path) -> str | None:
    """Return the package containing a Python file under packages/."""
    try:
        relative = path.resolve().relative_to((REPOSITORY_ROOT / "packages").resolve())
    except ValueError:
        return None

    parts = list(relative.with_suffix("").parts)
    if parts[-1] == "__init__":
        parts.pop()
    else:
        parts.pop()
    return ".".join(parts)


def _imported_names(node: ast.Import | ast.ImportFrom, path: Path) -> tuple[str, ...]:
    if isinstance(node, ast.Import):
        return tuple(alias.name for alias in node.names)

    module = node.module or ""
    if node.level:
        package = _package_for(path)
        if package is None:
            return ()
        package_parts = package.split(".")
        keep = len(package_parts) - (node.level - 1)
        if keep <= 0:
            return ()
        base = ".".join((*package_parts[:keep], *module.split(".")))
    else:
        base = module

    names = [base] if base else []
    names.extend(
        f"{base}.{alias.name}" if base else alias.name
        for alias in node.names
        if alias.name != "*"
    )
    return tuple(names)


def find_forbidden_imports(source: str, path: Path) -> tuple[Violation, ...]:
    tree = ast.parse(source, filename=str(path))
    violations: list[Violation] = []
    seen: set[tuple[int, str, str]] = set()

    for node in ast.walk(tree):
        if not isinstance(node, (ast.Import, ast.ImportFrom)):
            continue
        for imported_name in _imported_names(node, path):
            dependency = _dependency_for(imported_name)
            if dependency is None:
                continue
            key = (node.lineno, imported_name, dependency.prefix)
            if key not in seen:
                seen.add(key)
                violations.append(
                    Violation(path, node.lineno, imported_name, dependency)
                )

    return tuple(violations)


def test_domain_tree_has_no_forbidden_dependencies() -> None:
    violations = [
        violation
        for path in sorted(DOMAIN_ROOT.rglob("*.py"))
        for violation in find_forbidden_imports(path.read_text(encoding="utf-8"), path)
    ]

    assert not violations, "Forbidden domain dependencies:\n" + "\n".join(
        violation.describe() for violation in violations
    )


@pytest.mark.parametrize(
    ("source", "expected_import", "expected_category"),
    (
        ("import fastapi.routing", "fastapi.routing", "framework / WebSocket"),
        ("from sqlalchemy.orm import Session", "sqlalchemy.orm", "ORM / persistence"),
        ("import ollama", "ollama", "model provider"),
        ("from mcp.client import ClientSession", "mcp.client", "tool provider"),
        (
            "from dctm.infrastructure.persistence import schema",
            "dctm.infrastructure.persistence",
            "reversed domain-to-infrastructure dependency",
        ),
        (
            "from dctm import application",
            "dctm.application",
            "reversed domain-to-application dependency",
        ),
        (
            "from ...application import ports",
            "dctm.application",
            "reversed domain-to-application dependency",
        ),
        (
            "from packages.dctm.application import ports",
            "packages.dctm.application",
            "reversed domain-to-application dependency",
        ),
        (
            "from packages.dctm.infrastructure import persistence",
            "packages.dctm.infrastructure",
            "reversed domain-to-infrastructure dependency",
        ),
        (
            "from packages.dctm import application",
            "packages.dctm.application",
            "reversed domain-to-application dependency",
        ),
        (
            "from packages.dctm import infrastructure",
            "packages.dctm.infrastructure",
            "reversed domain-to-infrastructure dependency",
        ),
        (
            "import packages.dctm.application.services",
            "packages.dctm.application.services",
            "reversed domain-to-application dependency",
        ),
        (
            "import packages.dctm.infrastructure.persistence.sqlcipher",
            "packages.dctm.infrastructure.persistence.sqlcipher",
            "reversed domain-to-infrastructure dependency",
        ),
    ),
)
def test_detector_rejects_representative_forbidden_imports(
    source: str,
    expected_import: str,
    expected_category: str,
) -> None:
    path = DOMAIN_ROOT / "example" / "module.py"

    violations = find_forbidden_imports(source, path)

    assert violations
    diagnostic = "\n".join(violation.describe() for violation in violations)
    assert str(path) in diagnostic
    assert expected_import in diagnostic
    assert expected_category in diagnostic
    assert "Architecture §9.4" in diagnostic


@pytest.mark.parametrize(
    "source",
    (
        "from dataclasses import dataclass",
        "from pydantic import BaseModel, ConfigDict",
        "from dctm.domain.contracts import primitives",
        "from . import sibling",
    ),
)
def test_detector_accepts_allowed_imports(source: str) -> None:
    path = DOMAIN_ROOT / "example" / "module.py"

    assert find_forbidden_imports(source, path) == ()
