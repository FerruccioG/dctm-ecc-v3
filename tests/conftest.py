"""Fail-closed Gate Zero dependency preflight for pytest startup."""

from __future__ import annotations

from importlib import import_module, metadata
import sys
from typing import Mapping

import pytest


_EXPECTED_PYTHON = (3, 13, 15)
_EXPECTED_VERSIONS = {
    "pytest": "9.1.1",
    "pydantic": "2.13.5",
    "sqlcipher3": "0.6.2",
    "SQLAlchemy": "2.0.52",
    "alembic": "1.19.2",
}
_REQUIRED_MODULES = (
    "pydantic",
    "sqlcipher3.dbapi2",
    "sqlalchemy",
    "alembic",
)
_EXPECTED_SQLCIPHER = "4.12.0 community"


class GateZeroBlocked(RuntimeError):
    """Raised when the certified Gate Zero baseline is unavailable."""


def _validate_gate_zero(
    expected_versions: Mapping[str, str] = _EXPECTED_VERSIONS,
    expected_python: tuple[int, int, int] = _EXPECTED_PYTHON,
    expected_sqlcipher: str = _EXPECTED_SQLCIPHER,
) -> None:
    failures: list[str] = []
    observed_python = sys.version_info[:3]
    if observed_python != expected_python:
        failures.append(
            f"Python: expected {'.'.join(map(str, expected_python))}, "
            f"observed {'.'.join(map(str, observed_python))}"
        )

    for distribution, expected in expected_versions.items():
        try:
            observed = metadata.version(distribution)
        except metadata.PackageNotFoundError:
            observed = "not installed"
        except Exception as exc:  # fail closed on unreadable package metadata
            observed = f"metadata error ({type(exc).__name__}: {exc})"
        if observed != expected:
            failures.append(
                f"{distribution}: expected {expected}, observed {observed}"
            )

    imported: dict[str, object] = {}
    for module_name in _REQUIRED_MODULES:
        try:
            imported[module_name] = import_module(module_name)
        except Exception as exc:
            failures.append(
                f"{module_name}: expected importable, "
                f"observed {type(exc).__name__}: {exc}"
            )

    dbapi2 = imported.get("sqlcipher3.dbapi2")
    if dbapi2 is not None:
        connection = None
        cursor = None
        try:
            connection = dbapi2.connect(":memory:")
            cursor = connection.execute("PRAGMA cipher_version")
            row = cursor.fetchone()
            observed_cipher = None if row is None else row[0]
            if observed_cipher != expected_sqlcipher:
                failures.append(
                    "SQLCipher runtime: "
                    f"expected {expected_sqlcipher}, observed {observed_cipher!r}"
                )
        except Exception as exc:
            failures.append(
                "SQLCipher in-memory capability: expected operational, "
                f"observed {type(exc).__name__}: {exc}"
            )
        finally:
            if cursor is not None:
                try:
                    cursor.close()
                except Exception as exc:
                    failures.append(
                        "SQLCipher cursor cleanup: expected successful, "
                        f"observed {type(exc).__name__}: {exc}"
                    )
            if connection is not None:
                try:
                    connection.close()
                except Exception as exc:
                    failures.append(
                        "SQLCipher connection cleanup: expected successful, "
                        f"observed {type(exc).__name__}: {exc}"
                    )

    if failures:
        details = "\n".join(f"- {failure}" for failure in failures)
        raise GateZeroBlocked(f"BLOCKED — Gate Zero preflight failed:\n{details}")


def pytest_configure(config: pytest.Config) -> None:
    """Validate the certified toolchain before pytest collects tests."""
    del config
    try:
        _validate_gate_zero()
    except GateZeroBlocked as exc:
        raise pytest.UsageError(str(exc)) from exc
