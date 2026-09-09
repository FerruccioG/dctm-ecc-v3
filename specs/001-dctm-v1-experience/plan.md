# Implementation Plan: DCTM WOW V1 — Sprint 0.2 / Sprint 1 Readiness

**Branch**: `main` | **Date**: 2026-09-09 | **Spec**: [spec.md](spec.md)

**Authority**: `docs/DCTM_Bible_Spec_Kit_v1.0.0.md` → `docs/DCTM_WOW_V1_Final_Architecture_Plan_v1.0.1.md` → frozen `spec.md` → Spec Kit. Architecture v1.0.0 is superseded. This plan decomposes approved decisions and makes none.

## Summary

Prepare Sprint 1 to implement the risk-first DCTM V1 modular monolith. Sprint 0.2 establishes enforceable repository boundaries, versioned contracts, the 106-FR compliance register, separate 20-SC traceability, deterministic test doubles, and evidence conventions. Sprint 1 (Increment 1) delivers the constitutional kernel: typed canonical commands/events, sole transactional commit path, deterministic authority/policy, mandatory audit, and one safe human-controlled transition. No application feature is implemented here.

## Technical Context

**Language/Version**: Python 3.13; TypeScript with Svelte 5/SvelteKit  
**Dependencies**: FastAPI, Pydantic 2, SQLAlchemy 2 Core, Alembic; native Ollama behind Model Gateway; exact versions remain Gate Zero pins  
**Storage**: SQLCipher SQLite/WAL/`synchronous=FULL`; PyNaCl vault; rebuildable FTS5/NumPy projections  
**Testing**: Certified Gate Zero toolchain; deterministic doubles; property, contract, integration, E2E, security, fault, recovery, certification, and soak suites  
**Platform**: Ubuntu 26.04 VM on Windows; native Ollama over host-only Caddy mTLS; guest ext4 `/var/lib/dctm` on J:-backed block storage  
**Type**: Local single-node web application; modular-monolith backend, static browser UI, optional isolated media worker  
**Performance**: stop ≤300 ms p95; command ≤750 ms p95; commit-to-UI ≤500 ms p95; context ≤2 s p95; warm token ≤5 s median/≤12 s p95; cold token ≤45 s p95; restart ≤60 s; four-hour six-seat soak  
**Constraints**: one human; six active AI maximum; one writer/path; privacy/authority/context/integrity fail closed; no remote fallback/export; human preemption; Spec Kit/ECC/Codex development-only  
**Scope**: increments 0–7 are core; Increment 8 Media Preview is separate

No `NEEDS CLARIFICATION` remains. Approved deferred seam choices are preserved in [research.md](research.md).

## Constitution Check

*GATE: PASS before research; PASS after Phase 1 design.*

| Gate | Proof | Result |
|---|---|---|
| Authority supremacy | Sources/hashes recorded; frozen sources untouched | PASS |
| Inference/transparency | Provenance/disclosure contracts; reality claims prohibited | PASS |
| Context Before Speech | Scoped, fresh Context Manifest gates admission | PASS |
| Privacy | Restrictive visibility inheritance and pair-private non-interference | PASS |
| Human sovereignty | Human-only control/preemption; model/moderator non-authoritative | PASS |
| Character/continuity | Provider-independent identity; meeting survives sessions | PASS |
| Uncertainty/surprise | Claims, evidence, uncertainty and significance explicit | PASS |
| Canonical integrity | State, journal, audit and outbox commit atomically once | PASS |
| Approved baseline | Architecture §21 and certified Gate Zero only | PASS |
| Runtime separation | Spec Kit/ECC/Codex engineering-only | PASS |
| Traceability | 106 FR rows plus separate 20 SC rows; absence is BLOCKED | PASS |
| Governance stop | No redesign, conflict, or new high-level decision required | PASS |

Post-design: [data-model.md](data-model.md) and [contracts](contracts/README.md) preserve inward dependencies, gateways, visibility, the single writer, human authority, and separate media certification. No exception exists.

## Project Structure

### Planning artifacts

```text
specs/001-dctm-v1-experience/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── compliance-register.md
├── success-criteria-register.md
├── work-packages.md
├── assurance-plan.md
└── contracts/{README.md,v1-contract-catalog.md}
```

`tasks.md` is deliberately absent.

### Approved target layout (not created by this Plan)

```text
apps/{api,web,media-worker}/
packages/dctm/
├── domain/{authority,meeting,roster,session,privacy,floor,context,character,evidence,delivery,audit,recovery,contracts}/
├── application/{commands,queries,orchestration,ports,canonical_commit}/
└── infrastructure/{api,persistence,vault,projections,observability,model_gateway,capability_gateway,presentation,deployment}/
migrations/
tests/{architecture,contract,unit,property,integration,e2e,security,privacy,fault_injection,recovery,model_certification,soak}/
evidence/
ops/
```

Domain imports no framework/provider. Application depends on domain/ports. Infrastructure and apps depend inward. Domains never access another domain's tables. Only Canonical Commit writes. Ollama uses Model Gateway; tools/MCP use Capability Gateway; presentation consumes committed outbox records. Conformance tests enforce imports, gateway access, egress, and write-path uniqueness.

## Persistence and Migration

Meeting is the aggregate root. Canonical state, append-preserving journal, mandatory audit, and outbox intent share one SQLCipher transaction. Commands carry immutable IDs, expected aggregate version, idempotency, correlation/causation, policy version, and Recovery Epoch as applicable. Projections are disposable.

Alembic revisions are ordered, forward-verified, rollback-aware, and tested against encrypted production-shaped fixtures. Updates require a verified recovery point. Restore goes to a new location and verifies cryptography, schema, journal/audit chains, artifacts, delivery, and projections before human-approved promotion. Shared/sync/network live databases are forbidden.

## Sequence and Readiness

[work-packages.md](work-packages.md) preserves Increment 0 assurance; 1 constitutional kernel; 2 first complete turn; 3 shared deliberation; 4 privacy/continuity; 5 evidence/emergence; 6 operational hardening; 7 six-seat release candidate. Media Preview/Increment 8 remains separate.

Sprint 1 starts only after Increment 0 review passes: boundaries, contracts, registers, evidence schema, doubles, CI commands, threat model, migration plan, and install/backup/fault/model-certification obligations are ready. This Plan does not claim future evidence exists.

## Definition of Done

Each package links authority, FR/SC, ADR, control, positive/negative/boundary/adversarial scenarios, evidence, versions/hashes, observed outcome, and verdict. Missing evidence is `BLOCKED`. Hard controls use PASS/BLOCKED; experience uses separate human judgment. See [assurance-plan.md](assurance-plan.md).

## Governance

No clarification or STOP arose. Exact model build, token budgets, summary algorithm, backup cadence, optional provider, media packages/licenses, and performance supersession stay deferred within Architecture §26.2. Any boundary change or framework/model/database/protocol/security/topology substitution requires planning stop and human-approved superseding ADR.

## Complexity Tracking

No violation or exception requested.
