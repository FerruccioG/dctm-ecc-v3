"""Reject outer-layer imports of the canonical-state mutation boundary."""

from __future__ import annotations

import ast
from dataclasses import dataclass
from pathlib import Path

import pytest


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
PACKAGES_ROOT = REPOSITORY_ROOT / "packages" / "dctm"

AUTHORITY = (
    "canonical mutation control-path rule: outer layers must use approved "
    "command/admission/control boundaries; only Canonical Commit changes "
    "authoritative state (Architecture §8.1/§9.2/§15.1; T008)"
)

# The frozen material names this module, but does not yet freeze a callable.
# Keep exact mutation modules here so later additions do not widen an allowlist.
CANONICAL_MUTATION_MODULES = (
    "dctm.application.canonical_commit",
    "packages.dctm.application.canonical_commit",
)


@dataclass(frozen=True)
class Origin:
    root: Path
    category: str


# These roots come from plan.md's approved target layout. apps/web is a static
# TypeScript UI; Python files beneath it are test-only representative inputs.
# More-specific infrastructure roles precede the generic infrastructure root.
FORBIDDEN_ORIGINS = (
    Origin(Path("apps/web"), "UI (representative Python test path)"),
    Origin(
        Path("packages/dctm/infrastructure/model_gateway"),
        "model / Model Gateway",
    ),
    Origin(
        Path("packages/dctm/infrastructure/capability_gateway"),
        "tool / Capability Gateway",
    ),
    Origin(Path("packages/dctm/domain/delivery"), "delivery domain"),
    Origin(
        Path("packages/dctm/infrastructure/presentation"),
        "delivery / Presentation & Delivery",
    ),
    Origin(Path("packages/dctm/infrastructure"), "infrastructure"),
)

# T042 freezes this composition root as the narrow place that wires Canonical
# Commit to adapters. It composes the control path; it is not an initiating UI,
# model, tool, delivery, or infrastructure mutation entry point.
NON_ENTRYPOINT_COMPOSITION_ROOTS = (
    Path("packages/dctm/infrastructure/composition/kernel.py"),
)


@dataclass(frozen=True)
class MutationBoundaryViolation:
    path: Path
    category: str
    line: int
    imported_target: str

    def diagnostic(self) -> str:
        return (
            f"{self.path}:{self.line}: {self.category} directly imports canonical "
            f"mutation target {self.imported_target!r}; violates {AUTHORITY}"
        )


def _repository_path(path: Path) -> Path | None:
    candidate = path if path.is_absolute() else REPOSITORY_ROOT / path
    try:
        return candidate.resolve(strict=False).relative_to(REPOSITORY_ROOT.resolve())
    except ValueError:
        return None


def _is_within(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
    except ValueError:
        return False
    return True


def _origin_for(path: Path) -> Origin | None:
    repository_path = _repository_path(path)
    if repository_path is None or repository_path in NON_ENTRYPOINT_COMPOSITION_ROOTS:
        return None
    return next(
        (
            origin
            for origin in FORBIDDEN_ORIGINS
            if _is_within(repository_path, origin.root)
        ),
        None,
    )


def _package_for(path: Path) -> str | None:
    repository_path = _repository_path(path)
    packages = Path("packages")
    if repository_path is None or not _is_within(repository_path, packages):
        return None

    parts = list(repository_path.relative_to(packages).with_suffix("").parts)
    if parts[-1] == "__init__":
        parts.pop()
    else:
        parts.pop()
    return ".".join(parts)


def _imported_targets(
    node: ast.Import | ast.ImportFrom, path: Path
) -> tuple[str, ...]:
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

    targets = [base] if base else []
    targets.extend(
        f"{base}.{alias.name}" if base else alias.name
        for alias in node.names
        if alias.name != "*"
    )
    return tuple(targets)


def _is_canonical_mutation_target(imported_target: str) -> bool:
    return any(
        imported_target == module or imported_target.startswith(f"{module}.")
        for module in CANONICAL_MUTATION_MODULES
    )


def find_direct_canonical_mutation_imports(
    source: str, path: Path
) -> tuple[MutationBoundaryViolation, ...]:
    origin = _origin_for(path)
    if origin is None:
        return ()

    tree = ast.parse(source, filename=str(path))
    violations: list[MutationBoundaryViolation] = []
    seen: set[tuple[int, str]] = set()
    for node in ast.walk(tree):
        if not isinstance(node, (ast.Import, ast.ImportFrom)):
            continue
        for target in _imported_targets(node, path):
            key = (node.lineno, target)
            if _is_canonical_mutation_target(target) and key not in seen:
                seen.add(key)
                violations.append(
                    MutationBoundaryViolation(
                        path=path,
                        category=origin.category,
                        line=node.lineno,
                        imported_target=target,
                    )
                )
    return tuple(violations)


def test_current_python_tree_has_no_outer_layer_canonical_mutation_imports() -> None:
    violations = [
        violation
        for path in sorted(PACKAGES_ROOT.rglob("*.py"))
        for violation in find_direct_canonical_mutation_imports(
            path.read_text(encoding="utf-8"), path
        )
    ]

    assert not violations, "Forbidden canonical mutation entry path(s):\n" + "\n".join(
        violation.diagnostic() for violation in violations
    )


@pytest.mark.parametrize(
    ("path", "source", "category", "target"),
    (
        (
            Path("apps/web/server.py"),
            "from dctm.application import canonical_commit",
            "UI",
            "dctm.application.canonical_commit",
        ),
        (
            Path("packages/dctm/infrastructure/model_gateway/client.py"),
            "import dctm.application.canonical_commit",
            "model / Model Gateway",
            "dctm.application.canonical_commit",
        ),
        (
            Path("packages/dctm/infrastructure/capability_gateway/runner.py"),
            "from dctm.application.canonical_commit import RepresentativeCommit",
            "tool / Capability Gateway",
            "dctm.application.canonical_commit.RepresentativeCommit",
        ),
        (
            Path("packages/dctm/domain/delivery/dispatcher.py"),
            "from packages.dctm.application import canonical_commit",
            "delivery domain",
            "packages.dctm.application.canonical_commit",
        ),
        (
            Path("packages/dctm/infrastructure/persistence/rogue.py"),
            "from ...application import canonical_commit",
            "infrastructure",
            "dctm.application.canonical_commit",
        ),
    ),
)
def test_rejects_direct_access_from_each_forbidden_origin_category(
    path: Path, source: str, category: str, target: str
) -> None:
    violations = find_direct_canonical_mutation_imports(source, path)

    assert violations
    diagnostic = "\n".join(violation.diagnostic() for violation in violations)
    assert str(path) in diagnostic
    assert category in diagnostic
    assert target in diagnostic
    assert ":1:" in diagnostic
    assert "Architecture §8.1/§9.2/§15.1; T008" in diagnostic


@pytest.mark.parametrize(
    ("path", "source", "target"),
    (
        (
            Path("packages/dctm/infrastructure/rogue.py"),
            "import dctm.application.canonical_commit",
            "dctm.application.canonical_commit",
        ),
        (
            Path("packages/dctm/infrastructure/rogue.py"),
            "from dctm.application import canonical_commit",
            "dctm.application.canonical_commit",
        ),
        (
            Path("packages/dctm/infrastructure/rogue.py"),
            "from dctm.application.canonical_commit import RepresentativeCommit",
            "dctm.application.canonical_commit.RepresentativeCommit",
        ),
        (
            Path("packages/dctm/infrastructure/rogue.py"),
            "import packages.dctm.application.canonical_commit",
            "packages.dctm.application.canonical_commit",
        ),
        (
            Path("packages/dctm/infrastructure/presentation/stream.py"),
            "from ...application.canonical_commit import RepresentativeCommit",
            "dctm.application.canonical_commit.RepresentativeCommit",
        ),
    ),
)
def test_rejects_alternate_canonical_import_spellings(
    path: Path, source: str, target: str
) -> None:
    violations = find_direct_canonical_mutation_imports(source, path)

    assert any(violation.imported_target == target for violation in violations)


@pytest.mark.parametrize(
    "source",
    (
        "from dataclasses import dataclass",
        "from pydantic import BaseModel",
        "from dctm.domain.contracts import commands",
        "from dctm.domain.session import queries",
        "from dctm.application import queries",
        "import dctm.application.orchestration",
    ),
)
def test_allows_imports_that_are_not_canonical_mutation_entry_points(
    source: str,
) -> None:
    path = Path("packages/dctm/infrastructure/presentation/reader.py")

    assert find_direct_canonical_mutation_imports(source, path) == ()


def test_unrelated_infrastructure_is_not_itself_a_violation() -> None:
    path = Path("packages/dctm/infrastructure/observability/metrics.py")

    assert find_direct_canonical_mutation_imports("import statistics", path) == ()


def test_frozen_composition_root_is_not_treated_as_an_outer_entry_point() -> None:
    path = Path("packages/dctm/infrastructure/composition/kernel.py")
    source = "from dctm.application import canonical_commit"

    assert find_direct_canonical_mutation_imports(source, path) == ()


@pytest.mark.parametrize(
    "path",
    (
        Path("packages/dctm/infrastructure/rogue.py"),
        Path("packages/dctm/infrastructure/./rogue.py"),
        Path("packages/dctm/domain/../infrastructure/rogue.py"),
        REPOSITORY_ROOT / "packages/dctm/infrastructure/rogue.py",
    ),
)
def test_origin_classification_uses_normalized_repository_paths(path: Path) -> None:
    violations = find_direct_canonical_mutation_imports(
        "from dctm.application import canonical_commit", path
    )

    assert violations
    assert violations[0].category == "infrastructure"
