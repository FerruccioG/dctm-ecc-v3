# Contract Catalog v1

| Contract family | Required content | Producer → consumer | Reject when |
|---|---|---|---|
| Command v1 | principal/capability, operation, aggregate/version, idempotency, scope, correlation/causation, epoch | API/runtime → application/Canonical Commit | unauthorized, stale, malformed, duplicate mismatch |
| Domain Event v1 | aggregate, canonical sequence/version, causation, transition, visibility | Canonical Commit → projections/delivery | uncommitted, gap, bad hash/version |
| State v1 | explicit Meeting/Session/Presence/Privacy/Contribution/Tool/Delivery safety states | domain → commit/read ports | illegal transition |
| Policy Decision v1 | ALLOW/DENY/REQUIRE_HUMAN, rule/reason, constraints, expiry, version | Policy Decision Point → enforcement points | missing/stale/wrong scope/epoch |
| Authorization Lease v1 | principal, operation set, meeting/session/privacy scope, purpose, expiry/presence, epoch, revocation | human/policy → runtime/gateways | broadened, expired, disconnected, revoked |
| Visibility v1 | class, audience, source restrictions, disclosure linkage | Privacy/Context → every data boundary | derivation broadens scope |
| Context Package v1 | entitled social context, evidence/claims, character/relationship, exclusions | Context Builder → Model Gateway | readiness not proven |
| Context Manifest v1 | recipient/scope IDs, epoch/cutoff, source hashes, versions, tokens, exclusions, readiness | Context Builder → inference/admission | missing/stale/wrong-scope/invalid epoch |
| Model Request/Proposal v1 | manifest, character, template/schema/model/settings, deadline/cancel, priority; structured proposal metadata | runtime ↔ Model Gateway | direct authority/state effect or schema failure |
| Tool Request/Effect v1 | proposed capability, minimal authorized typed payload, effect state/reconciliation | runtime ↔ Capability Gateway | unauthorized data/effect; unknown repeat |
| Commit Result v1 | accepted/rejected, canonical version/sequence, event/audit/outbox IDs, reason | Canonical Commit → caller | partial commit claimed |
| Delivery v1 | committed outbox ref, presentation state, disclosure, cancellation, receipt | Delivery → browser/canonical command | proposal-only content; uncertain replay |
| Audit v1 | actor, policy/reason, operation, scope, versions, outcome, integrity link; minimized content | enforcement/commit → audit store | protected mutation lacks atomic record |
| Recovery v1 | epoch, verification checks, abandoned work, safety mode, required human action | Recovery Controller → UI/runtime | unsupported schema/integrity/privacy uncertainty |
| Evidence Record v1 | authority/FR/SC/ADR/control/scenario, environment versions, expected/observed, artifact hash, verdict | assurance runner/reviewer → dossier | missing proof or unverifiable artifact |

HTTP carries typed commands/queries; WebSocket carries committed live events and delivery reconciliation. Neither browser nor socket owns canonical state. Model access is only Model Gateway, tool/MCP access only Capability Gateway, and persistence writes only Canonical Commit.
