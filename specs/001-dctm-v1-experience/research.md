# Phase 0 Research: Authority-Bounded Resolution

No web research or upgrade was performed; frozen authority and the certified Gate Zero environment control.

| Topic | Decision | Rationale | Rejected alternatives |
|---|---|---|---|
| Boundary | Pure domain, application ports/use cases, inward adapters, composition apps | Architecture §§8–9; ADR-004–007, 123 | Distributed services; cross-domain table access |
| Persistence | One Canonical Commit atomically writes SQLCipher state, journal, audit, outbox; projections rebuild | §§11,15; ADR-060–070,126–129 | Multiple writers, shared-folder SQLite, Postgres/Redis/vector DB |
| Contracts | Versioned Pydantic envelopes and Model/Capability/Delivery/Persistence/Audit/Recovery ports | §§9,13,18,28.2 | Runtime agent framework, direct providers, untyped payloads |
| Stack | Preserve Python/FastAPI, SvelteKit, SQLCipher, local Ollama, local observability and Gate Zero pins | §§20–21; ADR-123–143 | Upgrade/substitution not authorized |
| Assurance | Individual 106-FR rows; separate 20-SC rows; absent evidence is BLOCKED | §§24.3,25.1,27; ADR-165–182,195,199 | Aggregate claims; treating SCs as FRs |
| Deferred seams | Retain §26.2 timing for model, budgets, summaries, backup cadence, provider, media licenses, performance | Boundaries fixed; choices intentionally deferred | Premature selection |

No `NEEDS CLARIFICATION`, conflict, or authority insufficiency remains for Sprint 0.2/Sprint 1 readiness.
