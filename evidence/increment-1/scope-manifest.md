# DCTM WOW V1 — Sprint 1 Scope Manifest

## Identity and provenance

- Product: DCTM WOW V1
- Sprint: Sprint 1
- Architecture increment: Increment 1 — Constitutional Kernel
- Task: T001
- Accepted Sprint 0.2 planning baseline commit: `d2bcc50`
- Current approved Sprint 1 task-baseline commit (execution provenance): `639b45d`

The Sprint 1 task baseline is recorded separately as execution provenance and does not replace the accepted Sprint 0.2 planning baseline.

## Frozen authorities

The following frozen-authority files have no content difference from commit `d2bcc50`:

| Repository path | SHA-256 |
|---|---|
| `docs/DCTM_Bible_Spec_Kit_v1.0.0.md` | `d02fda1526813949619eff9ef63262b4a89e198a5e12e9a616ccccd26c9798b9` |
| `docs/DCTM_WOW_V1_Final_Architecture_Plan_v1.0.1.md` | `0a2a18cc560ec946f0c8d57a305c8847a0028d20facc29eb1f6ad6d3ebb21299` |
| `specs/001-dctm-v1-experience/spec.md` | `7cedb147704e075a226bde65a563212eab52bf9b20c53f50f12998b9f2e97d42` |

## Sprint 1 allowlist

Increment 1 is limited to the Constitutional Kernel:

- versioned canonical commands/events needed by Increment 1;
- one canonical writer / Canonical Commit path;
- deterministic human authority and policy enforcement;
- canonical state persistence required by the Increment 1 transition;
- atomic state + journal + mandatory audit + outbox behavior;
- optimistic concurrency/idempotency and related constitutional controls required by the approved tasks;
- one safe human-controlled Session `CREATED -> ACTIVE` transition; and
- only the narrow encrypted migration/restart/fault seams required to prove Increment 1.

## Explicit Increment 2+ exclusions

Sprint 1 does **not** implement:

- First Complete Turn;
- Context Package / Context Manifest runtime;
- model request/proposal/admission loops;
- participant speech;
- shared deliberation;
- multi-character behavior;
- floor arbitration beyond anything strictly required by Increment 1;
- private aside / privacy continuity features;
- evidence/emergence features;
- Capability Gateway/tool execution;
- Model Gateway/model access;
- browser UI / visual WOW;
- six-seat release-candidate campaigns;
- voice;
- avatar;
- animation;
- translation/subtitles;
- Media Preview;
- backup/restore subsystem;
- disaster recovery;
- recovery-controller implementation;
- update/rollback framework;
- damaged-store recovery campaigns; or
- other Increment 6 Operational Hardening beyond the bounded Increment 1 proof already approved.

## Governance boundary

Any need to redesign, reinterpret, materially alter, resolve a contradiction in, or make a new high-level decision about the frozen Bible, specification, architecture, or ADRs requires:

**VOICE CONFERENCE REQUIRED — DEVELOPMENT/PLANNING STOPPED.**
