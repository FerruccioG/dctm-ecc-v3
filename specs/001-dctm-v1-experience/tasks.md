# Tasks: DCTM WOW V1 — Sprint 1 Constitutional Kernel

**Input**: Frozen Bible and Architecture v1.0.1; frozen `spec.md`; accepted Sprint 0.2 planning baseline at `d2bcc50`; design documents in `specs/001-dctm-v1-experience/`

**Sprint boundary**: Architecture Increment 1 only. This plan delivers canonical commands/events, one canonical writer/path, deterministic authority/policy enforcement, atomic canonical state + journal/audit/outbox behavior, and one safe human-controlled `Session CREATED → ACTIVE` transition. It does not implement a conversational turn or any Increment 2+ feature.

**Tests**: TDD is mandatory. Test tasks precede their corresponding implementation tasks; implementation begins only after the test has been observed failing for the intended reason.

**Task format**: `- [ ] Txxx [P?] [Story?] Description with exact file path`

## Phase 1: Setup and Scope Guardrails

**Purpose**: Establish the smallest Sprint 1 package/test layout and fail early if the accepted Gate Zero toolchain is unavailable. No dependency is installed or upgraded by this phase.

- [x] T001 Record the Sprint 1 Increment 1 scope allowlist, explicit Increment 2+ exclusions, frozen-authority hashes, and baseline commit `d2bcc50` in `evidence/increment-1/scope-manifest.md`
- [x] T002 Add a Gate Zero preflight that verifies Python 3.13, pytest, Pydantic 2, SQLCipher, SQLAlchemy 2 Core, and Alembic resolve at the already-certified pins and exits BLOCKED without installing or upgrading anything in `tests/conftest.py`
- [x] T003 Create the inward-dependency Python package boundaries with empty package initializers under `packages/dctm/domain/__init__.py`, `packages/dctm/application/__init__.py`, and `packages/dctm/infrastructure/__init__.py`
- [ ] T004 [P] Create the Sprint 1 test package layout with empty package initializers under `tests/architecture/__init__.py`, `tests/contract/__init__.py`, `tests/unit/__init__.py`, `tests/property/__init__.py`, `tests/integration/__init__.py`, `tests/fault_injection/__init__.py`, and `tests/recovery/__init__.py`
- [ ] T005 Define deterministic UUID, clock, and recovery-epoch test doubles without runtime/provider dependencies in `tests/doubles/kernel.py`

**Checkpoint**: Scope and certified-toolchain preflight are explicit; no runtime feature exists.

---

## Phase 2: Foundational Contracts and Architecture Boundaries

**Purpose**: Freeze executable Increment 1 boundaries before implementing the story. This phase blocks all story work.

### Tests first

- [ ] T006 [P] Add architecture tests rejecting framework, ORM, provider, UI, model, tool, and infrastructure imports from domain modules in `tests/architecture/test_domain_dependencies.py`
- [ ] T007 [P] Add architecture tests rejecting persistence writes outside `packages/dctm/application/canonical_commit.py` and its persistence port adapter in `tests/architecture/test_single_writer.py`
- [ ] T008 [P] Add architecture tests rejecting direct canonical-state mutation entry points from UI, model, tool, delivery, and infrastructure namespaces in `tests/architecture/test_canonical_mutation_boundaries.py`
- [ ] T009 [P] Add command-envelope contract tests for schema version, immutable IDs, principal/capability, operation, aggregate and expected version, idempotency, scope, correlation, causation, policy version, and recovery epoch in `tests/contract/test_command_v1.py`
- [ ] T010 [P] Add domain-event contract tests for committed aggregate identity, canonical sequence/version, causation, transition, visibility, schema version, and integrity link in `tests/contract/test_domain_event_v1.py`
- [ ] T011 [P] Add policy-decision contract tests for `ALLOW`, `DENY`, and `REQUIRE_HUMAN` plus reason, constraints, scope, expiry, version, and epoch in `tests/contract/test_policy_decision_v1.py`
- [ ] T012 [P] Add commit-result contract tests that prohibit partial-success claims and require accepted/rejected status plus event, audit, and outbox identifiers when accepted in `tests/contract/test_commit_result_v1.py`
- [ ] T013 [P] Add audit and outbox contract tests requiring minimized actor/decision/outcome metadata, integrity linkage, committed-event reference, and no proposal-only payload in `tests/contract/test_audit_outbox_v1.py`

### Minimal contract implementation

- [ ] T014 Implement shared opaque identifiers, schema-version value objects, correlation metadata, and validation errors in `packages/dctm/domain/contracts/primitives.py`
- [ ] T015 Implement the canonical command v1 envelope as immutable Pydantic domain contract in `packages/dctm/domain/contracts/commands.py`
- [ ] T016 [P] Implement the canonical domain event v1 envelope as immutable Pydantic domain contract in `packages/dctm/domain/contracts/events.py`
- [ ] T017 [P] Implement policy decision v1 and deterministic reason-code contracts in `packages/dctm/domain/authority/decisions.py`
- [ ] T018 [P] Implement commit result v1 contracts with explicit rejection and no partial-success state in `packages/dctm/domain/contracts/commit_results.py`
- [ ] T019 [P] Implement minimized audit-record and committed outbox-intent contracts in `packages/dctm/domain/audit/records.py` and `packages/dctm/domain/delivery/outbox.py`
- [ ] T020 Define inward-facing repository, transaction, policy-decision, journal, audit, and outbox ports with no infrastructure imports in `packages/dctm/application/ports/kernel.py`
- [ ] T021 Run the contract and architecture tests and record expected/observed results and hashes as BLOCKED on any failure in `evidence/increment-1/foundation/conformance.md`

**Checkpoint**: Versioned kernel contracts and inward ports pass; conformance tests mechanically guard the sole write path.

---

## Phase 3: User Story 1 — Human Activates a Created Session (Priority: P1) 🎯 Sprint 1 MVP

**Goal**: An authenticated human principal can activate an existing `CREATED` session exactly once through Canonical Commit. Non-human, malformed, stale, duplicate-mismatch, wrong-scope, wrong-policy-version, wrong-epoch, and illegal-transition commands fail closed without canonical side effects. A successful transition atomically changes state, advances version/sequence, appends the journal and mandatory audit records, and creates one committed outbox intent.

**Independent Test**: Given a persisted meeting and `CREATED` session, submit the typed activation command as the authenticated human and verify one atomic `ACTIVE` state/event/audit/outbox result. Repeat with adversarial identities and metadata, injected failures at every transaction stage, and a process restart; verify denial or rollback leaves no partial canonical result and the accepted result survives intact.

### Tests first — domain and policy

- [ ] T022 [P] [US1] Add unit tests for `CREATED → ACTIVE` and rejection of activation from `ACTIVE`, `SUSPENDED`, or `CLOSED` in `tests/unit/test_session_activation.py`
- [ ] T023 [P] [US1] Add positive and negative authority tests proving only the authenticated V1 human principal can activate a session and model/character/moderator/tool/infrastructure actors cannot in `tests/unit/test_activation_authority.py`
- [ ] T024 [P] [US1] Add boundary tests for exact meeting/session scope, policy version, expiry boundary, and recovery epoch in `tests/unit/test_activation_policy_boundaries.py`
- [ ] T025 [P] [US1] Add adversarial tests for forged role claims, transferred capability, missing principal, malformed identifiers, and unknown operations in `tests/unit/test_activation_policy_adversarial.py`
- [ ] T026 [P] [US1] Add property tests generating actors, scopes, versions, epochs, and session states to prove only the exact human-authorized transition can return `ALLOW` in `tests/property/test_activation_authority_invariants.py`

### Tests first — canonical transaction and persistence

- [ ] T027 [P] [US1] Add integration tests proving accepted activation atomically writes session state, aggregate version/sequence, one journal event, one mandatory audit record, and one outbox intent in `tests/integration/test_activation_atomic_commit.py`
- [ ] T028 [P] [US1] Add negative integration tests proving stale expected version, duplicate command with changed payload, sequence collision, invalid epoch, and failed policy produce zero writes in `tests/integration/test_activation_rejections.py`
- [ ] T029 [P] [US1] Add idempotency tests proving an exact retry returns the original commit result without advancing state, sequence, journal, audit, or outbox in `tests/integration/test_activation_idempotency.py`
- [ ] T030 [P] [US1] Add fault-injection tests at state, journal, audit, outbox, and commit boundaries proving total rollback and mandatory-audit fail-closed behavior in `tests/fault_injection/test_activation_transaction_faults.py`
- [ ] T031 [P] [US1] Add restart tests proving committed activation and its journal/audit/outbox integrity survive reopen while uncommitted work disappears in `tests/recovery/test_activation_restart.py`
- [ ] T032 [P] [US1] Add migration tests for creation and upgrade of the Increment 1 encrypted canonical schema, failed-migration transactional rollback leaving the source store safe and unchanged, unsupported-schema fail-closed behavior, and encrypted-store reopen in `tests/recovery/test_increment_1_migration.py`

### Domain and application implementation

- [ ] T033 [US1] Implement the minimal `Meeting`, `Session`, `HumanPrincipal`, session-state, aggregate-version, and canonical-sequence domain types needed only for activation in `packages/dctm/domain/session/entities.py`
- [ ] T034 [US1] Implement the pure session activation invariant and event derivation without persistence or framework imports in `packages/dctm/domain/session/transitions.py`
- [ ] T035 [US1] Implement the deterministic activation policy rules for human sovereignty, exact scope, policy version, expiry, expected version, and recovery epoch in `packages/dctm/domain/authority/activation_policy.py`
- [ ] T036 [US1] Implement the typed `ActivateSession` application command handler that delegates every mutation to Canonical Commit in `packages/dctm/application/commands/activate_session.py`

### Persistence and sole commit path

- [ ] T037 [US1] Define the minimal Increment 1 SQLAlchemy Core metadata for meetings, sessions, command idempotency, journal, mandatory audit, and outbox with constraints for versions, sequences, and references in `packages/dctm/infrastructure/persistence/schema.py`
- [ ] T038 [US1] Create the ordered Alembic Increment 1 revision for the encrypted canonical-kernel schema in `migrations/versions/0001_constitutional_kernel.py`
- [ ] T039 [US1] Implement the SQLCipher connection and transaction adapter with WAL, `synchronous=FULL`, foreign keys, exclusive single-writer ownership, and no plaintext fallback in `packages/dctm/infrastructure/persistence/sqlcipher.py`
- [ ] T040 [US1] Implement read-only aggregate loading plus journal/audit/outbox append operations behind the kernel persistence ports in `packages/dctm/infrastructure/persistence/kernel_repository.py`
- [ ] T041 [US1] Implement Canonical Commit to revalidate policy/invariants inside one transaction, enforce optimistic version/idempotency/epoch, write state+journal+audit+outbox atomically, and return the commit result in `packages/dctm/application/canonical_commit.py`
- [ ] T042 [US1] Add the narrow application composition function that wires activation policy, Canonical Commit, and SQLCipher adapters without exposing repository mutation handles in `packages/dctm/infrastructure/composition/kernel.py`

### Story verification and evidence

- [ ] T043 [US1] Run the unit, contract, property, integration, fault-injection, recovery, and architecture suites and capture commands, environment versions, expected/observed outcomes, and artifact hashes in `evidence/increment-1/session-activation/test-report.md`
- [ ] T044 [US1] Record positive, negative, boundary, and adversarial human-authority scenario evidence with trace links to Constitution VI, ADR-008–013, and applicable control rows in `evidence/increment-1/session-activation/authority-evidence.md`
- [ ] T045 [US1] Record atomicity and injected-fault proof showing no partial state/journal/audit/outbox outcome, including mandatory-audit failure, in `evidence/increment-1/session-activation/transaction-evidence.md`
- [ ] T046 [US1] Record Increment 1 encrypted canonical-schema creation/upgrade, failed-migration source-store safety or transactional rollback, unsupported-schema fail-closed behavior, encrypted-store reopen, and committed-state survival across an ordinary application/process restart with reproducible hashes, explicitly excluding backup/restore and Increment 6 recovery work, in `evidence/increment-1/session-activation/migration-restart-evidence.md`

**Checkpoint**: The only Sprint 1 transition is independently testable and evidenced; no HTTP endpoint, browser UI, model, context manifest, participant speech, or delivery streaming is present.

---

## Phase 4: Independent Assurance and Increment Exit

**Purpose**: Obtain assurance evidence separate from builder self-certification and produce a human-reviewable Increment 1 verdict. This phase adds no product behavior.

- [ ] T047 [P] Re-run the architecture and single-writer conformance suite from a clean checkout/worktree and record the independent observed results and hashes in `evidence/increment-1/independent-qa/architecture-conformance.md`
- [ ] T048 [P] Re-run the authority scenario matrix without using builder-authored expected outputs as the oracle and record independent PASS/BLOCKED findings in `evidence/increment-1/independent-qa/authority-review.md`
- [ ] T049 [P] Independently inspect the encrypted database after success and every injected fault to reconcile canonical state, journal, audit, and outbox cardinality/hash linkage in `evidence/increment-1/independent-qa/atomicity-review.md`
- [ ] T050 Independently reproduce the bounded Increment 1 migration, fail-closed, encrypted-store reopen, and ordinary application/process restart proof from a fresh encrypted fixture—without backup/restore, recovery-controller, disaster-recovery, update/rollback, or damaged-store recovery work—and record any discrepancy as BLOCKED in `evidence/increment-1/independent-qa/recovery-review.md`
- [ ] T051 Audit Sprint 1 changes against the scope manifest and record absence of Increment 2+ code, speculative gateways, UI/model/tool mutation paths, and frozen-authority modifications in `evidence/increment-1/independent-qa/scope-audit.md`
- [ ] T052 Assemble the Increment 1 evidence index linking authority → ADR/control → scenario/assertion → artifact/hash → PASS/BLOCKED, with missing evidence forced to BLOCKED, in `evidence/increment-1/index.md`
- [ ] T053 Write the Increment 1 operational note covering certified startup preflight, encrypted-store location, migration/restart procedure, known limitations, and safe failure behavior in `ops/increment-1-kernel.md`
- [ ] T054 Prepare the human sovereign review record with independent-QA findings and an unsigned PASS/BLOCKED decision field reserved for Ferruccio Guicciardi in `evidence/increment-1/human-review.md`

**Checkpoint**: Sprint 1 may be declared complete only after T054 is human-reviewed and every required hard-control verdict is PASS. Code existence alone is insufficient.

---

## Dependencies & Execution Order

### Phase dependencies

- **Phase 1** has no dependencies. T001 → T002 → T003; T004 may run alongside T003; T005 follows the test layout.
- **Phase 2** depends on Phase 1. T006–T013 are failing tests written first; T014–T020 implement the contracts/ports; T021 verifies the foundation.
- **Phase 3 / US1** depends on T021. T022–T032 must be written and observed failing before their corresponding implementation. Domain/policy work T033–T035 precedes handler T036. Schema/migration/adapters T037–T040 precede Canonical Commit T041; composition T042 follows T036 and T041. Evidence T043–T046 follows passing implementation.
- **Phase 4** depends on T043–T046. Independent checks T047–T049 may run in parallel; T050 follows fixture availability; T051 follows all code changes; T052–T054 are sequential exit packaging.

### Critical dependency chain

`T001 → T002 → T003/T004 → T005 → T006–T013 → T014–T020 → T021 → T022–T032 → T033–T036 → T037–T042 → T043–T046 → T047–T051 → T052 → T053 → T054`

### Safe parallel opportunities

- T004 can run while T003 creates production package boundaries.
- T006–T013 target distinct conformance/contract test files and can run concurrently.
- T016–T019 target independent contract modules after T014.
- T022–T026 and T027–T032 target separate test files; each group can run concurrently once shared fixtures/contracts exist.
- T047–T049 are independent assurance activities and must be performed by an Independent QA/Assurance role or agent distinct from the builder.
- Tasks sharing `canonical_commit.py`, persistence schema/repository files, migrations, or the same evidence index are intentionally sequential and carry no `[P]` marker.

## Parallel Example: User Story 1

```text
After T021, dispatch in parallel:
T022 session-transition unit tests
T023 authority positive/negative tests
T024 policy boundary tests
T025 adversarial policy tests
T026 authority property tests
T027 atomic-commit integration tests
T028 rejection integration tests
T029 idempotency tests
T030 transaction fault tests
T031 restart tests
T032 migration tests
```

## Implementation Strategy

1. Establish scope/toolchain guardrails and architecture tests.
2. Make the versioned kernel contracts executable before behavior.
3. Write and observe all US1 tests failing for their intended reason.
4. Implement the pure domain transition and deterministic human-authority policy.
5. Implement the minimum encrypted schema and sole transactional commit path.
6. Prove positive, negative, boundary, adversarial, atomic-fault, migration, and restart behavior.
7. Require independent assurance and Ferruccio's human verdict before Increment 2 planning or implementation begins.

## Sprint 1 Exit Criteria

- Canonical command, event, policy-decision, commit-result, audit, and outbox schemas are versioned and contract-tested.
- Architecture tests enforce inward dependencies, approved gateway boundaries, and Canonical Commit as the sole authoritative write path.
- Deterministic authority/policy permits only the authenticated human principal, exact scope/version/epoch, and legal `CREATED → ACTIVE` transition; all tested invalid and adversarial variants fail closed.
- One accepted command atomically updates canonical session state, aggregate version/sequence, append-preserving journal, mandatory audit, and outbox; no injected failure leaves a partial result.
- Exact retries are idempotent; changed-payload duplicates and stale versions are rejected.
- The encrypted schema migrates forward under the approved migration mechanism; failure recovery and unsupported schema behavior are evidenced.
- A committed transition, journal/audit integrity, and outbox survive restart; uncommitted work does not.
- Positive, negative, boundary, adversarial, property/invariant, transaction/fault, migration, restart, contract, unit, integration, and architecture evidence exists with reproducible hashes.
- Independent QA/Assurance has reproduced the applicable controls; the builder does not self-certify completion.
- Missing evidence or any hard-control failure yields `BLOCKED`; Ferruccio Guicciardi retains the final unsigned human sovereign decision in T054.
- No Increment 2+ behavior or speculative cathedral scaffolding is present.

## Explicitly Deferred

No Sprint 1 task implements First Complete Turn, Context Manifest/model proposal/admission/presentation loops, participant speech, shared deliberation, multi-character behavior, privacy aside/continuity, evidence/emergence, six-seat release-candidate campaigns, Media Preview, voice, avatar, animation, translation/subtitles, visual WOW, browser UI, model access, tool access, or later operational hardening beyond the narrow migration/restart/fault seams needed to prove Increment 1.
