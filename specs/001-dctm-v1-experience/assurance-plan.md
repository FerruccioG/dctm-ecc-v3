# Assurance and Operational Readiness Plan

## Evidence chain and verdicts

Every proof follows `authority → FR/SC → ADR → control → scenario/assertion → evidence artifact/hash → verdict`. Deterministic, architecture, security, privacy, recovery, and integrity verdicts are `PASS` or `BLOCKED`; missing evidence is `BLOCKED`. Experiential review remains separate: `READY`, `READY WITH DECLARED LIMITATIONS`, or `NOT READY` with observations by dimension.

## Required campaigns

| Campaign | Minimum obligations | Planned evidence |
|---|---|---|
| Threat model | assets, actors, trust zones, entry points, STRIDE-style threats, privacy flows, injection, secrets, browser/origin/CSRF, bridge/mTLS, egress, artifacts, supply chain, mitigations/residual risk | versioned model, data-flow diagrams, control/scenario links, review record |
| Privacy non-interference | seeded pair-private canaries absent from unauthorized prompts, outputs, summaries, embeddings, logs, tools, exports, behavior | sink-by-sink results and hashes; any leak BLOCKED |
| Backup/restore | encrypted DB/vault/config/model refs/key instructions; restore to new location; verify crypto/schema/chains/artifacts/delivery/projections; human promotion | backup manifest, restore report, recovery timing, approval record |
| Fault injection | crash/failure at commit, audit, disk, model, context, dispatch, presentation, migration, backup, restore, key, bridge, clock | before/after state, epoch, containment mode, recovery outcome |
| Model certification | declared digest/prompt/schema/settings; ≥20 recorded critical trials; structure, context, distinction, uncertainty, latency | outputs/hashes and aggregate verdict; zero privacy/authority/context violations |
| Clean install/update | pinned offline inventory, hashes, SBOM, secrets provisioning, ext4/storage, mTLS/ports, SQLCipher, model presence, startup preflight; recovery point/rollback | clean-machine log, preflight report, vulnerability/secret scan, update/rollback rehearsal |
| Architecture conformance | inward imports, no direct provider/tool/write access, one Uvicorn worker, local-only egress/export | automated dependency/gateway/write-path/network reports |
| Canonical regression | Naming of America plus independent scenarios covering private exchange, return, evidence, close/reopen, crash and delivery | browser/E2E traces, audit correlation, expected/observed verdicts |
| Capacity/performance | binding latency budgets and four-hour six-seat workload without crash, invariant failure, GPU OOM, or unreconciled state | target-hardware telemetry (local/redacted), resource and correctness report |
| Human experience | designed and open encounters; WOW, presence, immersion, warmth, distinction, fire, recap, coherence | cited observations and rationale; no composite score |

## Evidence hygiene

Evidence names include increment, scenario ID, environment/config/model/prompt/schema versions, timestamp, and content hash. Secrets and unnecessary private content are excluded. Generated evidence is immutable for a dossier version; corrections create a new record. An LLM evaluator may assist discovery but is never sole proof. The signed release dossier requires Ferruccio's human sign-off.
