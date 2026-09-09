# Risk-First Work Packages

These packages preserve Architecture §24 order. Detailed executable tasks belong to a later `tasks.md` workflow.

| Increment | Package/outcome | Exit evidence |
|---|---|---|
| 0 | Assurance foundation: repository boundaries, schemas, ADR ledger, 106-FR/20-SC registers, CI gates, deterministic doubles | conformance checks, contract validation, traceability audit, evidence schema, reviewed readiness verdict |
| 1 | Constitutional kernel: canonical commands/events, one writer/path, authority/policy, atomic audit/outbox, one safe human transition | positive/negative/boundary/adversarial authority tests; transaction/fault proof; migration/restart evidence |
| 2 | First complete turn: grant→entitled manifest→local model proposal→admission→commit→stream→receipt | stale/wrong-scope/cancel/provider failure cases; delivery reconciliation; disclosure |
| 3 | Shared deliberation: distinct participants, bids, single grant, direct address, moderator overlay, interrupt | multi-party/property tests; human-preemption latency; moderator/seat negatives |
| 4 | Privacy and continuity: pair-private aside, shared pause, disclosure, saved meeting, reopen, absence/catch-up | non-interference canaries across every sink; crash/reopen/asymmetric history evidence |
| 5 | Evidence and emergence: local import, quarantine/provenance/claims, uncertainty, capability lifecycle, surprise gate | injection/path/tamper tests; effect reconciliation; coherent consequence evidence |
| 6 | Operational hardening: encryption, epochs, delivery uncertainty, security, install/update, backup/restore, fault handling | threat campaign, restore rehearsal, fault matrix, offline inventory/SBOM, clean-install proof |
| 7 | Six-seat release candidate: full regression/adversarial coverage, capacity soak, model certification, signed dossier | four-hour soak; zero critical violations; conformance and human sign-off package |
| Media Preview (8) | Separately enabled/certified voice/avatar/camera/translation/subtitles | independent consent/provenance/disclosure/privacy/resource/fallback certification; never core gate |

## Package Definition of Done

An increment is complete only when end-to-end behavior; authority links; versioned contracts/configuration; canonical/audit/delivery transitions; positive, negative, boundary, adversarial and failure scenarios; restart behavior; privacy/authority proof; operational guidance; limitations; reproducible artifact hashes; and release verdict are present. Missing required evidence is `BLOCKED`. No package self-approves an ADR deviation.
