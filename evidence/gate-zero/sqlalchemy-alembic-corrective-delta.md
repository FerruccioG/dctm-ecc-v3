# Gate Zero Corrective Delta — SQLAlchemy and Alembic

## Identity

- Product: DCTM WOW V1
- Date certified: 2026-09-15
- Trigger: Sprint 1 task T002
- Parent repository checkpoint: `6417461`
- Classification: Gate Zero corrective implementation-baseline delta
- Architecture change: No
- Bible/specification change: No

## Reason for corrective delta

T002 requires the Gate Zero preflight to verify the already-certified persistence-stack dependencies.

Independent inspection established that the approved architecture specifies:

- SQLAlchemy 2 Core for persistence access
- Alembic for migrations

and the Sprint 0.2 plan states that exact versions remain Gate Zero pins.

However, neither SQLAlchemy nor Alembic had an exact repository pin or an installed distribution in the certified `.venv`.

T002 therefore correctly stopped with:

`BLOCKED — CERTIFIED GATE ZERO PIN NOT PROVABLE`

No version was invented and no T002 implementation was performed while the baseline was incomplete.

## Corrective pins certified on 2026-09-15

| Component | Certified version |
|---|---:|
| Python | 3.13.15 |
| pytest | 9.1.1 |
| Pydantic | 2.13.5 |
| sqlcipher3 | 0.6.2 |
| SQLCipher runtime | 4.12.0 community |
| SQLAlchemy | 2.0.52 |
| Alembic | 1.19.2 |

The SQLAlchemy and Alembic pins above are a corrective Gate Zero delta certified on 2026-09-15. They are not represented as having been part of the original Gate Zero environment.

## Locked transitive additions

The resulting locked dependency closure additionally introduced:

- greenlet 3.5.6
- Mako 1.4.1
- MarkupSafe 3.0.3

No previously certified direct dependency version was replaced by the corrective sync.

## Validation evidence

The candidate SQLAlchemy/Alembic pair was first validated in an isolated Python 3.13.15 environment outside the repository and outside the project `.venv`.

Results:

- SQLAlchemy 2.0.52 import/version verification: PASS
- Alembic 1.19.2 import/version verification: PASS
- SQLAlchemy Core in-memory persistence probe: PASS
- Alembic SQLite migration context probe: PASS

A second isolated validation used the actual DCTM SQLCipher Python path:

- sqlcipher3 0.6.2
- SQLCipher 4.12.0 community
- SQLAlchemy 2.0.52
- Alembic 1.19.2

Results:

- SQLCipher connection: PASS
- SQLAlchemy Core over SQLCipher: PASS
- encrypted-table create/insert/select probe: PASS
- Alembic migration context over the same connection: PASS

The exact locked dependency closure was then synchronized into the project `.venv`.

Post-sync results:

- exact direct-version baseline: PASS
- `uv pip check`: PASS
- SQLCipher runtime 4.12.0 community: PASS
- SQLAlchemy Core over SQLCipher: PASS
- Alembic context over SQLCipher-backed connection: PASS

## Repository mutation boundary

The corrective dependency baseline changes are limited to:

- `pyproject.toml`
- `uv.lock`
- `evidence/gate-zero/sqlalchemy-alembic-corrective-delta.md`

No frozen Bible, Architecture, specification, Sprint plan, task definition, application code, domain code, infrastructure implementation, migration, or test implementation was changed by this corrective delta.

## T002 status

The original T002 blocker is removed.

T002 itself is not complete and must resume separately.

The Gate Zero preflight in `tests/conftest.py` remains subject to independent implementation and verification.
