# Data Model: Canonical State and Governed Derivations

## Rules

- `Meeting` is the persistent aggregate root; closing `Session` never destroys it.
- All canonical mutations enter through Canonical Commit with optimistic version, idempotency, sequence, Recovery Epoch, audit, and outbox.
- Derived data inherits the most restrictive source visibility and never outranks canonical sources.
- IDs are opaque/immutable; timestamps never override canonical sequence plus Recovery Epoch.

## Canonical entities

| Entity | Required fields/relationships | Invariant or lifecycle |
|---|---|---|
| Meeting | id, purpose, default tone, lifecycle, version, sequence; sessions | persists across sessions |
| Session | id, meeting_id, state, recovery_epoch, human_presence_lease | CREATED→ACTIVE→SUSPENDED/ CLOSED; resume human-only |
| HumanPrincipal | id, authentication reference | exactly one V1 sovereign principal |
| Character | id, profile/provenance/config versions | independent of model, voice, avatar, session |
| SeatAssignment | meeting_id, character_id, role overlay, activation/removal sequence | ≤6 active; absence does not free; moderator uses seat |
| Presence | seat_id, PRESENT/TEMPORARILY_ABSENT/CATCHING_UP | absent cannot observe/speak; return requires readiness |
| Relationship | participants, visibility, state/version, sources | durable, scoped, may be asymmetric |
| PrivacyScope | session_id, human_id, character_id, state, entry/exit | exactly human+one AI; shared room paused |
| FloorBid/Grant | speaker, scope, intent/reason, expiry, epoch | ≤1 current grant; human revocation immediate |
| Contribution | speaker, content reference, provenance, grant, manifest, admission, delivery | PROPOSED→VALIDATED→COMMITTED→PRESENTING→PERCEIVED; terminal rejection/uncertainty states |
| MemoryItem | purpose, durability, visibility, source IDs/hashes, confidence | derivative cannot broaden source visibility |
| Artifact/Evidence/Claim | hash, acquisition, confidence, visibility, provenance; claim-source links | untrusted/quarantined until admitted; claim ≠ evidence |
| AuthorizationLease | principal, meeting/session/scope, operations, purpose, expiry/presence, epoch | scoped, revocable, non-transferable; epoch invalidates |
| ToolInvocation | proposal, authorization, payload hash, dispatch/effect | EFFECT_UNKNOWN blocks blind retry |
| DeliveryRecord | contribution/outbox, presentation, receipt, uncertainty | only acknowledged PERCEIVED enters perceived history |
| RecoveryEpoch | meeting/session, monotonic value, cause/report | invalidates grants, manifests, jobs, leases |
| AuditRecord | actor, decision, operation, scope, versions, outcome, prior/current hashes | append-preserving and atomic for protected changes |

## Visibility

`MEETING_SHARED`, `PARTICIPANT_PRIVATE`, `PAIR_PRIVATE`, `SYSTEM_PROTECTED`, and `PUBLIC_EVIDENCE` are versioned values. Any derivation computes the meet of all source restrictions. Human disclosure creates a new shared item linked to—but never relabeling—the private source.

## Transaction and migration constraints

One transaction validates policy/invariants, changes relational state, advances aggregate sequence/version, appends journal and mandatory audit, and creates outbox intent. Uniqueness covers command idempotency and sequence; foreign keys preserve aggregate/scope ownership; checks enforce enumerated states and pair membership. SQLCipher/Alembic migration evidence includes preflight, backup point, forward verification, failure rollback/restore, and new-location promotion approval.

## Derived products

Context Packages/Manifests, working memory, summaries, projections, FTS, embeddings, caches, and UI models are rebuildable. Every Context Manifest records recipient/scope, meeting/session/privacy IDs, Recovery Epoch, cutoff sequence, selected source hashes, exclusions, policy/summary/prompt/model versions, token accounting, and readiness verdict. Missing, stale, wrong-scope, or invalidated manifests block inference/admission.
