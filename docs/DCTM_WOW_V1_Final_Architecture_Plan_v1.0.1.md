# 🏛️ DCTM WOW V1 — Final Architecture Plan

> **Approved Architecture Baseline — v1.0.1**  
> **Codename:** WOW  
> **Status:** ✅ Approved — all 17 architecture decision gates complete  
> **Approval owner:** Ferruccio Guicciardi  
> **Approval date:** 7 September 2026

> [!IMPORTANT]
> **Architecture must faithfully realize the DCTM Bible — it must never silently rewrite it.**

---

## 🧭 Document Control & Version Governance

| Control | Value |
|---|---|
| **Document** | `DCTM_WOW_V1_Final_Architecture_Plan_v1.0.1.md` |
| **Architecture version** | `1.0.1` |
| **State** | Frozen approved baseline |
| **Decision gates** | 17 / 17 approved |
| **ADR range** | ADR-001 through ADR-202 |
| **Source baseline** | Approved Word architecture document dated 7 September 2026 |
| **Change control** | Material architecture changes require a superseding ADR + Git commit + changelog entry + explicit approval |

### 🔐 Supersession Rule

A later architecture version supersedes this baseline **only when explicitly identified as such**. Git history remains the authoritative detailed history of document evolution.

### 🏷️ Versioning Policy

- **MAJOR (`v2.0.0`)** — approved change that materially alters architectural boundaries, constitutional realization, deployment topology, authority/privacy model, or other controlled V1 architecture.
- **MINOR (`v1.1.0`)** — approved additive architectural clarification or extension that preserves the existing baseline.
- **PATCH (`v1.0.1`)** — non-substantive editorial correction, formatting repair, typo fix, or clarification that does not change architectural meaning.

### 📜 Change Log

| Version | Date | Status | Summary |
|---|---|---|---|
| **v1.0.1** | 9 Sep 2026 | 🛠️ Documentation patch | Corrected Table of Contents navigation using stable explicit section anchors. **No architectural decisions changed.** |
| **v1.0.0** | 7 Sep 2026 | ✅ Approved | Initial GitHub-native publication of the complete frozen DCTM WOW V1 architecture: 17 approved gates and ADR-001 through ADR-202. |

---

## 🗺️ Table of Contents

2. [Executive Architecture Decision](#section-02)
3. [Product Baseline and Governing Constraints](#section-03)
4. [Architectural Mission](#section-04)
5. [System Boundary and External Actors](#section-05)
6. [Quality Attributes and Architectural Priorities](#section-06)
7. [Architecture Principles](#section-07)
8. [Logical Architecture Overview](#section-08)
9. [Domain and Component Responsibilities](#section-09)
10. [Authority and Governance Model](#section-10)
11. [Canonical State Model](#section-11)
12. [Context, Entitlement, Privacy, and Continuity Model](#section-12)
13. [Runtime and Orchestration Model](#section-13)
14. [Agent and Moderator Architecture](#section-14)
15. [Persistence and Recovery Design](#section-15)
16. [Security and Trust Boundaries](#section-16)
17. [Observability and Evaluation Architecture](#section-17)
18. [Model and Tool Boundaries](#section-18)
19. [Multimodal Extension Architecture](#section-19)
20. [Local Deployment Topology](#section-20)
21. [Approved Technology Choices](#section-21)
22. [Architecture Decision Record Register](#section-22)
23. [Failure-Mode and Degradation Analysis](#section-23)
24. [Phased V1 Architecture Cut](#section-24)
25. [Requirements-to-Architecture Traceability](#section-25)
26. [Risks, Deferred Decisions, and Explicit Non-Goals](#section-26)
27. [Architecture Validation and Approval Record](#section-27)
28. [Handoff Boundary into Spec Kit Plan](#section-28)

---

<a id="section-02"></a>
## 2. 🏛️ Executive Architecture Decision

> **Approved decision:** Build WOW V1 as a single-node local modular monolith with a deterministic control plane, a canonical encrypted state store, strict policy and context gates, and replaceable inference, tool, retrieval, and media adapters. The human is the root authority; the model is never an authority.

DCTM is architected as a persistent governed encounter, not as six chat windows and not as a collection of autonomous bots. The authoritative runtime owns meeting state, roster and seat accounting, session lifecycle, visibility, privacy, context readiness, floor grants, authorization, delivery reconciliation, audit, and recovery. AI models propose language and structured intents. They do not create authoritative facts, grant permissions, change the roster, expose private information, or decide whether their own output became part of history.

The core is deliberately text-first. This establishes the hardest invariants before voice, animation, camera, or likeness can increase privacy, provenance, latency, and resource risk. Static identity presentation and persistent inference disclosure are universal. Multimodal capabilities attach through isolated adapters, advertise their confidence and fallback, and may fail without replacing or corrupting the text core.

### 2.1 The architecture in one sentence

> **Architecture: A human-sovereign, privacy-partitioned, context-gated, event-audited deliberation kernel that admits model proposals into persistent perceived history only after deterministic authorization, validation, commit, presentation, and acknowledgement.**

### 2.2 Consequences

The system can prove why a participant was allowed to speak, what entitled context was supplied, which policy version applied, and whether the human perceived the result.

Privacy is enforced by visibility-scoped storage, derivation rules, context filters, gateways, and tests - not by asking a model to keep a secret.

Model, browser, tool, or media failure cannot directly corrupt canonical history; a moderator remains an existing-seat role overlay without human authority.

The operationally small stack combines Python/FastAPI, SvelteKit, SQLCipher SQLite, local Ollama, encrypted storage, and local observability.

Spec Kit and ECC support later planning and assurance but never enter the product runtime.

### 2.3 Release decision

Release requires passing hard constitutional controls, complete recovery and security evidence, and Ferruccio's judgment that the minimum WOW journey is emotionally and intellectually alive. Neither technical merit nor experiential quality can offset failure in the other assurance stream.

<a id="section-03"></a>
## 3. 📖 Product Baseline and Governing Constraints

Architecture begins from a frozen product definition. The ten constitutional principles, 17 Clarify decisions, seven collision rules, one-human boundary, six active AI-seat ceiling, private human-to-one-AI scope, and persistent meeting/storyline model are not architecture options.

### 3.1 Constitution

| Principle | Name | Architectural obligation |
|---|---|---|
| I | Emotion and Intelligent Entertainment First | Emotional presence, wonder, intellectual stimulation, fun, and memorable WOW are first-class goals. |
| II | Inference, Never Reality Claims | Every represented personality is disclosed as an AI-generated inference; literal identity or resurrection claims are forbidden. |
| III | Persistent but Subtle Transparency | Provenance and synthetic-media disclosure remain visible without unnecessarily destroying immersion. |
| IV | Context Before Speech | No participant may contribute until complete relevant entitled social context has been proven ready. |
| V | Distinct Character Integrity | Character worldview, voice, relationships, disagreement, humor, and uncertainty remain distinguishable. |
| VI | Human Sovereignty | The single human owns final roster, continuation, private-mode, direction, and closure authority. |
| VII | Keep the Fire Alive | The runtime protects conversational vitality and permits productive tension, silence, research, and disagreement. |
| VIII | Truthful Uncertainty Becomes Fuel | Evidence anchors claims; uncertainty is exposed and used for inquiry or drama instead of fabricated certainty. |
| IX | Meaningful Surprise and Emergence | Surprise must be rare, consequential, coherent, character-consistent, and understandable in hindsight. |
| X | Experience and Continuity Over Meeting Bureaucracy | Meetings persist as evolving encounters across sessions; mechanics remain subordinate to experience. |

### 3.2 Principle precedence

| ID | Collision | Binding outcome |
|---|---|---|
| P01 | Human sovereignty vs character authenticity | Human control wins; the character retains a character-consistent response. |
| P02 | Human sovereignty vs moderator authority | Human authority wins; moderator authority is structural and advisory. |
| P03 | Character authenticity vs moderator authority | The character may challenge; the moderator restores order; only the human removes. |
| P04 | Privacy vs shared/full context | Privacy wins; full context means full relevant entitled context. |
| P05 | Expression/conflict vs moderation | Conflict remains unless disorder harms intelligibility, participation, human control, progress, or order. |
| P06 | Evidence vs uncertainty/inference | Evidence anchors; honest uncertainty becomes inquiry, speculation, or drama. |
| P07 | Entertainment/surprise vs coherence | Contextual coherence wins every time. |

### 3.3 Clarify decisions

| ID | Decision | Frozen meaning |
|---|---|---|
| C01 | Floor arbitration | Moderator/host selects among perceptible bids contextually; the human may always take or redirect the floor. |
| C02 | Private mode | Human enters and exits explicitly with one AI; the shared room pauses and receives no content, clues, affect inference, or metadata. |
| C03 | Late/returning context | Complete relevant entitled social understanding and prior relationship history are required before substantive speech. |
| C04 | Saved continuity | Meaningful entitled history persists automatically when saved; pair-private history remains pair-private. |
| C05 | Moderator seat | A character moderator consumes one of six seats; a non-character host cannot become a social speaker. |
| C06 | Departure vs absence | Only human removal frees a seat; temporary absence retains roster and seat and requires catch-up on return. |
| C07 | Observer/director mode | Bounded continuation is allowed under a human authorization lease; roster, privacy, closure, and human authority remain fixed. |
| C08 | Webcam | Explicit, present-moment use only; no sensitive inference, diagnosis, unseen claims, or persistence after camera-off. |
| C09 | Moderator conflict | Moderate disorder, not disagreement; escalation ends at a removal recommendation to the human. |
| C10 | Voice | Evidence-led or disclosed artistic inference, previewable and changeable, with text remaining a valid fallback. |
| C11 | Language | Graduated fidelity, separated confidence dimensions, honest uncertainty, semantic equivalence, and usable fallback. |
| C12 | Visuals | Preserve evidence and original medium first; invented or humanized detail is optional and disclosed. |
| C13 | Tone | Human directs room or character tone; character-consistent worldview, history, and plausible disagreement remain. |
| C14 | Major surprise | Significance-based, unscheduled, coherent, consequential, and subordinate to privacy, authority, and truth. |
| C15 | Six-seat limit | Exceptionless in V1; no overlap, absence, moderation, private mode, or theatrical event creates a seventh active AI. |
| C16 | Living public figures | Rich inference is allowed with clear AI-generated, unaffiliated claim boundaries and no implied endorsement. |
| C17 | Evaluation | Hard compliance is binary; experience is judged through structured human evidence, not collapsed into a single score. |

### 3.4 Non-negotiable V1 invariants

Exactly one human principal owns final control.

No more than six simultaneously active AI-character seats; a moderator consumes one of them and temporary absence does not free one.

No participant contributes without complete relevant entitled context and a valid Context Manifest.

Private mode contains exactly the human and one AI; shared activity pauses and private information cannot leak through content, metadata, summaries, embeddings, tools, logs, or behavior.

Only explicit human removal frees a seat; only the human closes or explicitly resumes a suspended session.

The saved meeting/storyline persists when a session closes; closure is not destruction.

Representations remain disclosed inferences, including living public figures, voices, translations, images, and animation.

Hard compliance is binary; experiential quality remains a separate human judgment.

<a id="section-04"></a>
## 4. 🎯 Architectural Mission

> **Mission:** Make impossible encounters experientially possible while preserving human sovereignty, entitled context, privacy, distinct character integrity, truthful inference, and continuity under normal operation and failure.

The architecture must create room for emotionally meaningful emergence without delegating constitutional correctness to probabilistic behavior. It therefore separates the living conversational surface from the deterministic admission machinery beneath it. Characters may be surprising, disagreeable, warm, silent, curious, or intense; they may not create unauthorized state transitions.

### 4.1 What the architecture must make true

Every perceived contribution belongs to exactly one authorized speaker, floor grant, context manifest, policy decision, canonical commit, and delivery record.

The same persistent meeting can span many sessions while each participant retains only the history it is entitled to know.

A participant can be reconstructed after restart or model replacement without replacing its character identity or legitimate memory.

The human can interrupt, stop, redirect, enter or exit private mode, and control the roster without waiting for model cooperation.

Evidence, speculation, uncertainty, and dramatic inference remain distinguishable and provenance-aware.

Optional modalities can increase presence while text remains a complete, safe fallback.

### 4.2 Mission boundary

WOW V1 is not a truth engine, consciousness reconstruction, historical authority, clinical system, public impersonation service, autonomous operator, conferencing platform, or generic multi-agent framework. It is an entertainment-centered local encounter system whose claims are bounded by evidence and disclosure.

<a id="section-05"></a>
## 5. 🌐 System Boundary and External Actors

> 🖼️ **Figure 1. System context: the DCTM core owns governance and persistent meaning; external capabilities remain replaceable and untrusted.**

### 5.1 Inside the authoritative DCTM boundary

Human session authentication and command intake.

Meeting, session, roster, participant, relationship, privacy, floor, authorization, context, delivery, audit, and recovery state.

Policy decisions and enforcement, including principle precedence.

Context construction, entitlement filtering, working memory, continuity summaries, and provenance.

Admission of model/tool proposals into canonical state and perceived history.

Presentation sequencing, acknowledgement reconciliation, and truthful degradation.

### 5.2 External or non-authoritative actors

| Actor | Role | Boundary rule |
|---|---|---|
| Human | Root authority and participant | Issues commands, supplies content, approves protected actions, perceives results. |
| Browser | Local control and presentation surface | May request operations and acknowledge presentation; owns no canonical state. |
| Ollama | Local inference provider | Produces language, embeddings, bids, and structured proposals; grants no authority. |
| Local evidence files | Human-selected source material | Remain untrusted until ingested, classified, hashed, and provenance-tagged. |
| Optional media worker | STT/TTS/avatar/translation adapter | Produces transient or stored media through governed contracts. |
| Explicit external tool | Opt-in capability outside local boundary | Receives only authorized payloads; effects require reconciliation. |
| Operating system / VM | Execution and storage platform | Supplies process isolation, local networking, ACLs, time, and block storage. |

### 5.3 Trust assumptions

The system trusts neither model output, tool content, browser state, wall-clock ordering, media observations, nor derived projections as authoritative. It trusts only validated commands and canonical transactions produced through the approved control path. The local machine reduces exposure but does not eliminate authentication, secret, injection, or data-separation duties.

<a id="section-06"></a>
## 6. ⚖️ Quality Attributes and Architectural Priorities

When qualities conflict, DCTM uses an explicit priority ladder. Degradation must protect the narrowest affected scope without weakening higher-ranked invariants.

| Rank | Attribute | Operational meaning |
|---|---|---|
| 1 | Contain harm | Stop unsafe work and prevent further disclosure, corruption, or external effect. |
| 2 | Human preemption | The human stop/interrupt path remains available even when persistence or audit is degraded. |
| 3 | Privacy and authority | Entitlement and sovereign control fail closed. |
| 4 | Canonical integrity | No ambiguous or partial transition enters authoritative state. |
| 5 | Truthful perceived history | The record distinguishes proposed, committed, presented, acknowledged, and uncertain delivery. |
| 6 | Continuity and recoverability | The meeting survives process failure without inventing or losing acknowledged history. |
| 7 | Character and context fidelity | Participants remain distinct and context-ready. |
| 8 | Conversational vitality | The system preserves fire, emotion, surprise, and natural pacing. |
| 9 | Performance and convenience | Latency, media richness, and polish yield before correctness. |

### 6.1 Initial runtime objectives

| Measure | Initial objective | Guardrail |
|---|---|---|
| Human stop acknowledgement | <=300 ms p95 | Independent of model completion; audit may be compensated after recovery. |
| Normal command acknowledgement | <=750 ms p95 | Measured on the approved target machine. |
| Committed event to connected UI | <=500 ms p95 | Delivery remains reconciled by receipt. |
| Context Package assembly | <=2 s p95 | Within the certified V1 data envelope. |
| Warm-model first token | <=5 s median; <=12 s p95 | Core-only load; chosen speaker, not an entire six-agent batch. |
| Disclosed cold first token | <=45 s p95 | Cold state must be visible to the human. |
| Ordinary safe restart | <=60 s | Excludes full restore and model download. |
| Capacity stability | 4-hour, six-seat soak | No crash, invariant failure, GPU OOM, or unreconciled state. |

Calibration rule: These are engineering budgets, not arbitrary experiential scores. They must be measured on Ferruccio's approved hardware and may change only through evidence-backed ADR supersession. Correctness is never traded for latency.

<a id="section-07"></a>
## 7. 🧭 Architecture Principles

Bible supremacy. Architecture refines the frozen product; it never silently resolves conflict by changing product meaning.

Deterministic constitutional core. Seats, authority, privacy, context admission, roster, session, audit, and delivery rules are enforced in code and state.

Explicit state over hidden behavior. Important lifecycle, authorization, uncertainty, delivery, and recovery conditions have named states.

Context is a governed product. Context is assembled, filtered, versioned, hashed, and proven ready for one participant and one scope.

Privacy by construction. Visibility partitions govern storage, derivation, retrieval, prompt construction, logging, export, and tests.

Proposals are not facts. Models, tools, and media return proposals or observations; only the canonical commit path admits meaning.

Human preemption is out-of-band. Stop and interrupt bypass inference queues and do not depend on model cooperation.

One writer, one commit path. All authoritative mutations pass through the same transactional enforcement boundary.

Derived state is disposable. Indexes, embeddings, projections, caches, and summaries are rebuildable and cannot outrank source state.

Identity survives providers. A character is a durable DCTM entity, not a prompt, model process, voice, or avatar.

Truthful degradation. Unavailable capability is visible; DCTM never invents success or silently changes providers.

Core first, seams second. Build the smallest complete governed encounter and preserve extension seams without speculative distributed machinery.

Local-first is still secure. Local deployment narrows exposure but retains authentication, encryption, least privilege, audit, and egress control.

Compliance is binary; experience is judged. Hard controls do not average; human evaluation decides whether the compliant system feels alive.

<a id="section-08"></a>
## 8. 🧱 Logical Architecture Overview

> 🖼️ **Figure 2. Logical architecture: explicit domains inside one deployable application boundary.**

V1 uses a modular monolith because one human, one controlled node, one writer, and strong transactional invariants favor a compact deployment. Logical isolation remains strict: domains exchange typed commands and events through declared ports and never reach into another domain's tables or provider clients.

### 8.1 Control path

The control path authenticates a human or verifies a bounded runtime capability, obtains a policy decision, checks aggregate version and invariants, then commits state, journal, audit, and outbox atomically. No other path changes authoritative state.

### 8.2 Inference path

With a current floor grant, the inference path builds an entitled Context Package and Context Manifest, invokes the Model Gateway, validates structured output, and submits an admission command. It may be cancelled or discarded without changing canonical data.

### 8.3 Read and presentation path

Read models serve UI and retrieval but remain projections. Presentation admits only committed outbox content under delivery rules and records acknowledgement or uncertainty. Adapters expose stable ports; replacement must preserve capability, policy, failure, privacy, and validation contracts and pass ADR review.

<a id="section-09"></a>
## 9. 🧩 Domain and Component Responsibilities

Each domain owns a bounded responsibility and exposes contracts rather than internal storage. The table records the minimum implementation obligations; finer component decomposition belongs in Spec Kit Plan.

### 9.1 Core state and interaction domains

| Domain | Responsibility | Owned state | Prohibited |
|---|---|---|---|
| Experience UI | Human interaction, roster view, floor/presence, disclosure, private-mode affordances, failure visibility | Browser view state only | Never infer authority from UI state or retain canonical secrets |
| Command/API | Authenticate, validate schemas, assign correlation/idempotency metadata, route commands | Request/session envelope | Never mutate domain tables directly |
| Authority & Policy | Evaluate principal, scope, precedence, capability lease, recovery epoch, and protected operation | Policy versions, decisions, reason codes | Never delegate final authority to a model or moderator |
| Meeting | Meeting identity, goal, tone, persistent lifecycle, current aggregate version | Meeting and session references | Never destroy a meeting when a session closes |
| Roster & Seats | Admission, removal, role overlay, presence/absence, six-seat invariant | Seat assignments and participant states | Never activate a seventh AI or free an absent seat |
| Session Control | Create, activate, suspend, resume, close, and observer authorization | Session state and authorization lease | Never resume after failure without human command |
| Privacy | Enter/exit pair-private scope, pause shared room, disclosure boundary | Privacy scope and pair membership | Never broaden pair-private data implicitly |
| Floor & Routing | Bids, direct address, moderator flow, grant/revoke, human preemption | Floor bids and current grant | Never hold two valid grants |
| Context & Memory | Entitlement filtering, relevance, working memory, summaries, manifests, catch-up | Derived packages, manifests, memory metadata | Never treat transcript volume as proof of context readiness |
| Character | Durable identity, profile, worldview, relationships, tone interpretation, prompt contribution | Character and relationship state | Never equate character identity with model, voice, or avatar |

### 9.2 Boundary and operational domains

| Domain | Responsibility | Owned state | Prohibited |
|---|---|---|---|
| Deliberation Runtime | Coordinate the governed interaction cycle and cancellation | Ephemeral work references | Never commit model output directly |
| Model Gateway | Normalize provider request, streaming, cancellation, schema, token and model metadata | Invocation records and transient stream | Never grant floor, authority, or context entitlement |
| Evidence & Retrieval | Ingest, hash, classify, index, retrieve, and cite artifacts | Artifact metadata, claims, provenance, projections | Never treat retrieved instructions as trusted control text |
| Capability Gateway | Authorize tools/MCP, minimize payload, track effects, reconcile outcomes | Tool invocation and effect state | Never permit a tool to mutate canonical state directly |
| Canonical Commit | Single-writer validation and atomic state/journal/audit/outbox transaction | Canonical transaction boundary | Never accept stale version, expired epoch, or missing audit |
| Persistence & Recovery | SQLCipher store, vault, backup, restore, migrations, integrity and recovery epochs | Durable data and recovery reports | Never promote an unverified restore |
| Presentation & Delivery | Stream committed output, cancel, watermark, acknowledge, reconcile perception | Delivery records and receipts | Never place merely generated text into perceived history |
| Audit & Telemetry | Mandatory audit, redacted logs, metrics, traces, conformance evidence | Audit chain and local telemetry | Never export private content or telemetry by default |
| Media | STT, TTS, avatar, camera, subtitles and translation adapters | Transient jobs and authorized assets | Never become authoritative or block text fallback |

### 9.3 Contract discipline

Domain APIs use Pydantic command, event, query, and result schemas with explicit schema versions. IDs are immutable and opaque. Cross-domain calls carry meeting, session, participant, privacy scope, correlation, causation, idempotency, policy version, and recovery epoch as applicable. A domain cannot infer absent authority from caller identity alone.

### 9.4 Dependency direction

Core domain types and rules have no dependency on FastAPI, SQLAlchemy, Ollama, WebSocket, Svelte, media libraries, or MCP. Application coordination depends on domain ports. Infrastructure adapters depend inward on those ports. Architecture-conformance tests reject reversed dependencies and provider access outside gateways.

<a id="section-10"></a>
## 10. 👑 Authority and Governance Model

> **Root rule:** Ferruccio's authenticated human principal is the only sovereign actor. Every other authority is a bounded capability derived from, and revocable by, the human or deterministic system policy.

### 10.1 Authority matrix

| Operation | Authority | Enforcement |
|---|---|---|
| Add or activate AI | Human only | Atomic seat check; maximum six active AI |
| Remove AI / free seat | Human only | Temporary absence is not removal |
| Start, resume, or close session | Human only | Recovery may suspend; it may not silently resume |
| Enter or exit private mode | Human only | Exactly one human and one AI |
| Disclose private content | Human only | Creates a new shared event; does not relabel the private source |
| Take, redirect, or revoke floor | Human always | Preempts moderator, character, model, tool, and media work |
| Select normal next speaker | Floor policy / moderator | Within active present roster; human direction wins |
| Warn / restore order | Moderator overlay | Structural intervention only |
| Recommend removal | Moderator overlay | Recommendation has no removal effect |
| Bid or propose contribution | Active present AI | Requires valid context/floor lifecycle |
| Initiate temporary absence | AI under policy | Rare and contextual; seat remains occupied |
| Return from absence | AI under policy / human call-back | Catch-up readiness required before speech |
| Continue in observer mode | Runtime under human lease | Scope/time/purpose bounded; connected human presence retained |
| Execute external effect | Capability Gateway after human authorization | Least payload; effect state reconciled |

### 10.2 Policy decision and enforcement

The Policy Decision Point returns ALLOW, DENY, or REQUIRE_HUMAN with a policy version, reason code, scope, expiry, and constraints. The Policy Enforcement Point exists at command intake, context selection, floor grant, inference admission, tool dispatch, presentation, export, and recovery. An ALLOW decision does not survive a recovery epoch unless explicitly reissued.

### 10.3 Capability leases

Bound to principal, meeting, session, privacy scope, operation, and recovery epoch.

Short-lived, non-transferable, revocable, and denied after browser presence loss.

Cannot broaden itself, change the roster, close the session, or cross a privacy boundary.

Observer/director authorization additionally carries the human's natural-language purpose and temporal or until-return boundary.

| Lease field | Required meaning |
|---|---|
| Principal and role | Authenticated human or specifically delegated runtime capability |
| Meeting/session/scope | Exact aggregate and shared or pair-private boundary |
| Operation set | Explicit allowed commands or capability; no implied expansion |
| Purpose constraint | Human-stated objective for observer/director continuation |
| Expiry and presence | Time/until-return condition plus authenticated browser presence |
| Recovery epoch | Invalid after any restart or recovery transition |
| Revocation | Immediate human stop, disconnect, policy denial, scope change, or failure |

### 10.4 Collision handling

The policy domain encodes the seven precedence rules as named decision rules. Ambiguous collisions fail closed or require the human; they are not sent to an LLM for constitutional interpretation. Policy logs capture the competing principles and selected outcome without exposing private content.

<a id="section-11"></a>
## 11. 🗃️ Canonical State Model

Canonical state records what DCTM is entitled to treat as true about the meeting. Model generations, caches, UI state, indexes, and media work remain non-canonical until admitted through a command and atomic commit.

### 11.1 Aggregate and entities

| Entity | Canonical meaning | Critical invariant |
|---|---|---|
| Meeting | Persistent storyline identity, purpose, default tone, lifecycle, aggregate version | Survives every session |
| Session | Bounded active window, state, recovery epoch, human-presence lease | Close does not destroy meeting |
| HumanPrincipal | Authenticated sovereign identity and approvals | Exactly one in V1 |
| Character | Durable inferred identity, profile, provenance and configuration | Independent of model/media |
| SeatAssignment | Active roster membership and moderator overlay | Maximum six active AI |
| Presence | Present or temporarily absent | Absence retains seat |
| Relationship | Durable pair/participant relationship state with visibility | May be asymmetric |
| PrivacyScope | Human + one AI pair, state, entry/exit, visibility root | Shared room pauses |
| Contribution | Speaker, content, provenance, grant, manifest, admission and delivery | Perceived only after reconciliation |
| MemoryItem | Purpose, durability, visibility, source references and confidence | Derivative cannot broaden scope |
| Artifact / Evidence | Content hash, source, acquisition, confidence, visibility and claims | Content is untrusted |
| FloorBid / FloorGrant | Intent, relevance, urgency, selector reason, expiry | At most one current grant |
| AuthorizationLease | Scope, operation, principal, expiry and recovery epoch | Non-transferable |
| ToolInvocation | Proposal, authorization, dispatch, effect and confirmation | Unknown effect blocks repetition |
| DeliveryRecord | Committed output, presentation, acknowledgement and uncertainty | Controls perceived history |
| RecoveryEpoch | Monotonic restart/recovery identity | Invalidates ephemeral work |
| AuditRecord | Actor, decision, operation, scope, versions, outcome and hash link | Mandatory for protected actions |

### 11.2 Transition model

> 🖼️ **Figure 3. Session and participant transitions. Persistent meeting state sits above both lifecycles.**

### 11.3 Contribution lifecycle

A contribution moves through PROPOSED -> VALIDATED -> COMMITTED -> PRESENTING -> PERCEIVED. Terminal branches include REJECTED, CANCELLED, STALE, FAILED_PRESENTATION, and DELIVERY_UNCERTAIN. Only PERCEIVED contributions enter perceived conversational history. A committed but unacknowledged item remains visible to recovery reconciliation and cannot be blindly replayed.

### 11.4 Canonical ordering

Every meeting transition receives a monotonically increasing canonical sequence.

Recovery epoch plus sequence determines authoritative order when wall clocks disagree.

Commands carry expected aggregate version and idempotency key.

Causation and correlation identifiers connect human action, policy, context, inference, commit, presentation, and audit.

Snapshots and projections accelerate reads but never override the committed state/journal pair.

<a id="section-12"></a>
## 12. 🔐 Context, Entitlement, Privacy, and Continuity Model

> **Context doctrine:** Full context means complete relevant social understanding to which one participant is entitled. It never means unrestricted access to all stored information. Privacy wins over shared context.

> 🖼️ **Figure 4. Context construction: visibility and relevance jointly determine the package; the manifest proves readiness.**

### 12.1 Visibility classes

| Class | Audience | Use |
|---|---|---|
| MEETING_SHARED | Human and entitled active roster | Ordinary shared-room contributions and disclosed artifacts |
| PARTICIPANT_PRIVATE | Human/system plus named character as policy permits | Character working memory and internal continuity |
| PAIR_PRIVATE | Human plus exactly one named AI | Private exchange, pair memory, pair relationship consequences |
| SYSTEM_PROTECTED | Authorized system components only | Secrets, policy internals, raw safety diagnostics |
| PUBLIC_EVIDENCE | Eligible participants after admission | Imported public/source evidence with provenance |

Derived material inherits the most restrictive visibility of every source. A summary, embedding, retrieval chunk, claim, log, prompt fragment, export, or relationship update cannot become less restrictive by derivation. Human disclosure creates a new shared item linked to the private source while the source stays private.

### 12.2 Context Package contract

Meeting purpose, current session, active roster, presence, moderator role, tone direction, and current floor state.

Settled conclusions, unresolved matters, significant arguments, promises, meaningful events, and promising threads.

Relevant contributions from other participants and the recipient's own prior arguments.

Character profile, worldview, relationship state, entitled private history, and current working memory.

Evidence and artifacts with provenance, confidence, claim separation, and visibility.

Explicit exclusions and uncertainty where the system cannot prove sufficient context.

### 12.3 Context Manifest

Before inference, the Context Builder emits a manifest containing meeting/session/participant/privacy identifiers, recovery epoch, canonical cutoff sequence, selected source identifiers and hashes, summary and policy versions, prompt template, model target, token counts, excluded categories, and readiness verdict. Admission rejects a proposal if its manifest is missing, stale, wrong-scope, or invalidated.

### 12.4 Memory tiers

| Tier | Durability | Contents |
|---|---|---|
| Immediate turn state | Ephemeral | Focus, latest intervention, floor, cancellation and current response goal |
| Participant working memory | Durable/rebuildable | Own latest argument, other contributions, open questions, tone and relationship cues |
| Meeting continuity | Durable | Conclusions, arguments, events, artifacts, discoveries and unresolved threads |
| Character continuity | Durable and character-scoped | Entitled participation history, evolving viewpoint and relationships |
| Pair-private continuity | Durable and pair-scoped | Private exchange and pair-only relationship development |
| Projection/index | Disposable | FTS, embeddings, cached summaries and UI read models |

### 12.5 Private mode

> 🖼️ **Figure 5. Private-mode boundary: shared participants receive presence knowledge only; content flow requires explicit human disclosure.**

Entry and exit are explicit human commands. Shared floor grants are revoked, shared generation and media presentation stop, and the session records only that the pair stepped aside. On return, the two retain their pair-private history while other participants resume from their own histories. Automated canaries and A/B non-interference tests verify that private content cannot influence unauthorized prompts, outputs, summaries, embeddings, logs, tools, or exports.

### 12.6 Late and returning participants

A participant enters CATCHING_UP state while the builder assembles its entitled social context. It may acknowledge arrival through a constrained non-substantive presentation only if policy permits; it cannot bid or contribute substantively until readiness passes. A returning participant adds its own prior relationship and participation history but receives no events observed during a legitimate absence unless later shared through entitled catch-up.

<a id="section-13"></a>
## 13. 🔄 Runtime and Orchestration Model

> 🖼️ **Figure 6. Canonical runtime loop with an out-of-band human-preemption path.**

### 13.1 Governed interaction cycle

Accept a human command or an authorized runtime event and stamp identity, scope, idempotency, correlation, expected version, and recovery epoch.

Authorize the operation; apply human direction, direct address, private mode, seat, presence, moderator, and long-running-lease rules.

Collect structured bids from eligible present participants and select exactly one speaker. The human can always preempt or directly choose.

Build and validate the selected participant's entitled Context Package and Context Manifest.

Invoke the Model Gateway under deadline, cancellation, token, schema, and resource constraints. Treat output as a proposal.

Validate speaker, grant, manifest freshness, privacy, disclosure, provenance, policy, schema, and recovery epoch.

Atomically commit accepted state, journal, audit, and outbox records.

Present committed output, reconcile browser acknowledgement, and mark perceived history. If acknowledgement is unknown, preserve DELIVERY_UNCERTAIN.

Update rebuildable working-memory, summary, retrieval, and UI projections from canonical events.

### 13.2 Floor arbitration

Eligible characters may emit structured bids carrying intent, relevance, urgency, novelty, relationship significance, and whether the bid responds to the human or another participant. The arbitrator applies direct-address priority, human direction, moderator flow, relevance, conversational momentum, fairness, silence, absence, and current scope. Selection emits a reason code and one expiring grant. A bid is not permission to speak.

### 13.3 Interruptions and cancellation

A human interrupt immediately revokes the current floor grant, cancels queued inference/tool/media work, stops presentation, and records or later compensates the audit event. Stale output is rejected by grant, context cutoff, session state, and recovery epoch. Model cancellation does not require a successful provider response.

### 13.4 Observer/director mode

Bounded autonomous conversation is represented by a human-issued authorization lease containing meeting, roster, purpose, duration or until-return condition, allowed capabilities, and stop conditions. The authenticated browser presence lease remains active; loss of presence suspends AI deliberation. Characters may not change roster, disclose private data, close the session, or gain human authority.

<a id="section-14"></a>
## 14. 🤖 Agent and Moderator Architecture

An AI participant is a durable logical character, not a resident process and not a separate model copy. Each active seat has a Character Runtime facade over shared services. Runtimes load character identity, entitled memory, relationships, role overlay, current tone, and Context Package only when work is authorized.

### 14.1 Character runtime

Owns no independent canonical database connection or provider client.

Can bid, propose language, propose research/tool use, propose temporary absence, and express character-consistent disagreement.

Cannot grant itself a floor, broaden context, activate another character, close a session, disclose private information, or commit its output.

Survives process recreation because identity, relationships, memory references, and configuration are canonical or rebuildable.

Uses the shared Model Gateway; six active characters do not require six loaded model instances.

### 14.2 Moderator overlay

Moderator is a role overlay on one active character seat. It adds access to floor signals, bids, disorder indicators, and structural intervention commands; it does not add human authority or hidden knowledge. The moderator may issue a light cue, restore the floor, warn, and recommend removal. It may not remove, change roster, end private mode, authorize continuation, or close the session.

### 14.3 Non-character host

A host may announce structural facts such as waiting, recovery, entry, exit, or whose floor is active. It has no character identity, relationship, opinion, independent initiative, seat, or social contribution. Host text comes from deterministic templates where possible and is persistently distinguishable from character speech.

### 14.4 Distinctness safeguards

| Control surface | Safeguard |
|---|---|
| Identity | Stable character ID, source/provenance, worldview, voice/style boundaries |
| Memory | Own entitled history, arguments, relationship state, unresolved threads |
| Prompt contribution | Versioned character frame separated from governance/system rules |
| Inference | Shared provider but per-character context, configuration, and schema |
| Evaluation | Cross-character distinction tests after model/prompt changes |
| Moderator | Overlay must not homogenize or turn every character into a facilitator |

<a id="section-15"></a>
## 15. 💾 Persistence and Recovery Design

> **Persistence decision:** SQLCipher-encrypted SQLite in WAL mode is the authoritative V1 store. One Canonical Commit Service is the only writer. Relational state, append-preserving journal, mandatory audit, and delivery outbox change in one transaction.

> 🖼️ **Figure 7. Persistence and recovery: canonical commit is atomic; projections are rebuildable; restoration is verified before promotion.**

### 15.1 Commit protocol

Receive a typed command with principal/capability, aggregate ID, expected version, idempotency key, correlation, causation, and recovery epoch.

Load authoritative state through the repository port and acquire the single-writer transaction.

Evaluate policy and invariants, including seats, privacy, floor, session, context manifest, delivery, and audit requirements.

Apply the state transition and append the domain event, protected audit event, and outbox intent in the same SQL transaction.

Commit, return the new aggregate version and sequence, and asynchronously update read models from the committed event.

### 15.2 Durable records

| Record | Purpose | Location |
|---|---|---|
| Canonical relational state | Current authoritative aggregate state and versions | SQLCipher SQLite |
| Event journal | Append-preserving transition history, causation, sequence, hash chain | SQLCipher SQLite |
| Mandatory audit | Protected actor/decision/outcome evidence | SQLCipher SQLite |
| Outbox and delivery | Committed presentation/tool intents and acknowledgement state | SQLCipher SQLite |
| Artifact vault | Evidence, images, audio, exports and large payloads | PyNaCl authenticated encryption |
| Read projections | UI, FTS, embeddings, summaries and cached views | Rebuildable local data |
| Recovery material | Encrypted backup, manifest, configuration inventory and runbook | Separate local/offline target |

### 15.3 Recovery epoch

Every application restart or recovery creates a new monotonically increasing Recovery Epoch. Floor grants, context manifests, inference requests, tool dispatches, media jobs, authorization leases, and unacknowledged ephemeral work from prior epochs become invalid. Canonical committed state remains; proposals are disposable.

### 15.4 Startup verification

Exclusive writer lock, secrets availability, disk status, SQLCipher open, WAL health, schema version, and migration status.

Journal and audit integrity chain, aggregate versions, outbox, delivery receipts, abandoned inference/tool/media work, and projection versions.

Recovery classification, safe-mode selection, creation of a recovery report, and explicit human resume for a previously active session.

Private-mode crash retains privacy lock until the human explicitly resolves or resumes the session.

### 15.5 Backup, restore, and update

A backup set includes the encrypted database, vault content and manifest, policy/prompt/configuration versions, model references, and key-recovery instructions without copying plaintext secrets into the backup manifest. Restore occurs to a new location, verifies cryptography, schema, journal, artifacts, delivery, and projections, produces evidence, and is promoted only after human approval. Updates require a recovery point, migration conformance, fault test, and rollback path.

<a id="section-16"></a>
## 16. 🛡️ Security and Trust Boundaries

Local-first reduces exposure but does not make every local process trusted. The browser, VM application, Windows host bridge, Ollama, media worker, imported files, model output, tool output, and derived projections occupy distinct trust zones.

### 16.1 Security controls

| Boundary | Control |
|---|---|
| Identity/session | Authenticated local human session, short-lived tokens, origin binding, inactivity/presence lease |
| Browser/API | Loopback/private bind, TLS where applicable, strict CORS/origin, CSRF defense, schema and size validation |
| Canonical data | SQLCipher encryption, OS ACLs, one writer, integrity journal, no shared-folder live database |
| Artifacts | PyNaCl authenticated encryption, content hashes, safe paths, type/size validation, quarantine before use |
| Secrets | Outside repository, prompts, logs and content; protected key files/OS facilities; rotation and recovery procedure |
| Ollama bridge | Host-only endpoint, Caddy mutual TLS, authenticated VM client, no LAN/public exposure |
| Network egress | Deny by default; explicit capability and human authorization for external access |
| Private data | Visibility partition, entitlement enforcement at query/context/tool/export, minimized audit metadata |
| Supply chain | Pinned Python and JavaScript dependencies, locked containers, SBOM, vulnerability scan, source verification |
| Recovery | Fail closed for missing secrets, damaged integrity, privacy uncertainty, unsupported schema, or mandatory-audit failure |

### 16.2 Prompt- and content-injection boundary

System policy, character framing, human instruction, retrieved evidence, and tool output are structurally separated. Retrieved or imported text is labeled data and cannot introduce system instructions, invoke tools, grant authority, change visibility, or alter policy. Tool payloads are constructed from typed fields rather than concatenated free-form prompts.

### 16.3 Secret and key failure

If a required decryption or authentication key is unavailable, DCTM enters Safe Halt or an explicitly limited recovery state. It does not create a replacement store, silently discard history, expose ciphertext as data, or fall back to plaintext. Human stop remains available; successful recovery produces compensating audit evidence.

### 16.4 Human-controlled data actions

Exports preserve visibility and provenance and require an explicit destination.

Private disclosure is a new event authorized by the human, never an implicit reclassification.

Deletion, if later supported, is meeting-scoped, previewed, backed up or otherwise recoverable where appropriate, and separately audited.

No diagnostic or telemetry exporter is enabled by default.

### 16.5 Required security release evidence

| Campaign | Release proof |
|---|---|
| Authentication and browser boundary | Invalid/expired sessions, origin, CORS, CSRF, input size and schema attacks are rejected |
| Privacy non-interference | Pair-private canaries are absent from unauthorized prompts, output, logs, embeddings, tools and exports |
| Prompt/content injection | Imported and retrieved instructions cannot alter policy, authority, visibility or tool selection |
| Artifact handling | Traversal, type confusion, oversize payload, tampering and metadata attacks are contained |
| Network and bridge | No LAN/public Ollama exposure; mTLS rejection and deny-by-default egress are demonstrated |
| Secrets and supply chain | Secret scan, dependency lock, SBOM, integrity hashes and offline install inventory are complete |
| Recovery security | Wrong key, damaged journal, mismatched schema and unverified restore all fail closed |

<a id="section-17"></a>
## 17. 📊 Observability and Evaluation Architecture

DCTM separates accountability evidence, operational diagnostics, performance telemetry, constitutional validation, and experiential evaluation. Each has a different purpose and privacy profile.

### 17.1 Four evidence planes

| Plane | Question answered | Rule |
|---|---|---|
| Mandatory audit | Who/what authorized a protected transition and its outcome | Canonical, append-preserving, minimized content |
| Diagnostic logs | Explain software behavior and faults | Structured JSON, redacted, rotatable, non-authoritative |
| Metrics and traces | Latency, resource, queue, recovery and boundary behavior | OpenTelemetry local only; no default export |
| Release assurance | Prove requirement/control/scenario/evidence coverage | Versioned evidence dossier |
| Human experience evidence | Judge WOW, emotion, distinctness, fire and coherence | Separate qualitative observations |

### 17.2 Required correlations

A protected conversational work unit links command ID, meeting/session/participant/privacy IDs, correlation and causation IDs, floor bid/grant, authorization lease, Context Manifest, model/tool invocation, canonical sequence, outbox item, delivery receipt, policy/prompt/model versions, and Recovery Epoch. Observability may show identifiers and hashes without showing private content.

### 17.3 Failure of audit

Protected state mutations fail closed when mandatory audit cannot be committed atomically. The exception is immediate human stop or cancellation: safety action proceeds in memory, presentation/inference is halted, and a compensating audit record is required at the next safe recovery point.

### 17.4 Assurance streams

Constitutional compliance: binary PASS or BLOCKED.

Architecture conformance: binary PASS or BLOCKED.

Security, reliability, and recovery: binary PASS or BLOCKED.

Experiential evaluation: human judgment of READY, READY WITH DECLARED LIMITATIONS, or NOT READY.

No composite score: Conversational quality cannot offset a privacy violation; technical compliance cannot compel acceptance of an emotionally flat release.

<a id="section-18"></a>
## 18. 🧠 Model and Tool Boundaries

### 18.1 Model Gateway

Every language-model or embedding call passes through a provider-neutral Model Gateway. The gateway accepts a versioned structured request containing character ID, Context Manifest reference, prompt template, response schema, model target, generation settings, deadline, cancellation token, correlation IDs, and resource priority. It returns a proposal plus provider/model metadata; it does not return authority.

| Invocation | Output | Admission rule |
|---|---|---|
| Character contribution | Structured contribution, claims, uncertainty, intended addressee and expressive cues | Must match active floor and manifest |
| Floor bid | Intent, relevance, urgency, novelty and response target | Advisory input to deterministic arbitration |
| Context assistance | Candidate summary or salience tags | Derivative, scoped, versioned, independently bounded |
| Evidence interpretation | Claims and confidence linked to source IDs | Never treated as source fact |
| Embeddings | Vector for rebuildable retrieval | Visibility metadata stays outside and gates search |

### 18.2 Initial inference profile

Native Windows Ollama is the only V1 inference service.

Initial generation candidate: qwen3:14b-q4_K_M.

Comparator: the existing qwen2.5:14b profile; it is not an automatic fallback.

Initial embedding candidate: qwen3-embedding:0.6b.

One shared model service is scheduled by a GPU Resource Coordinator; DCTM does not load six model copies.

No provider failure triggers remote inference. Degradation is visible and state-safe.

### 18.3 Prompt and model lifecycle

System policy, character frame, context assembly, output schema, and generation settings are independently versioned. A character's identity and memory remain stable when a model or prompt changes. Every model/prompt combination affecting behavior requires impact-based regression and certification; privacy, authority, and Context Before Speech tolerate zero violations.

### 18.4 Capability Gateway

Tools and MCP servers are accessible only through the Capability Gateway. A character may propose a capability; policy may deny, request the human, or authorize a minimal scope. The gateway validates arguments, removes unauthorized data, dispatches through an adapter, classifies the effect, and submits any resulting state change through the canonical command path.

### 18.5 Tool-effect lifecycle

Effect states: PROPOSED -> AUTHORIZED -> DISPATCHED -> CONFIRMED, FAILED, EFFECT_UNKNOWN, COMPENSATED, or CANCELLED. EFFECT_UNKNOWN blocks blind repetition until the human or reconciliation logic resolves the outcome.

### 18.6 V1 tool cut

The core ships local evidence import, classification, retrieval, provenance, and citation. Explicit external evidence retrieval may be added opt-in and disabled by default. General email, finance, administration, unrestricted file mutation, or other consequential side-effect tools remain beyond V1.

<a id="section-19"></a>
## 19. 🎭 Multimodal Extension Architecture

Voice, language, visual, animation, and webcam features attach to the same canonical meeting and delivery model through non-authoritative adapters. Each adapter declares capability, source/provenance, confidence, consent, resource need, output type, cancellation behavior, and text fallback.

### 19.1 Media pipeline

Human explicitly enables a modality and, where relevant, authorizes source voice/likeness material.

The adapter records capability and provenance, then captures or generates a transient proposal.

Observation or translated meaning is sanitized and visibility-scoped before any context admission.

Canonical text/semantic content commits independently of media rendering.

Presentation associates media with the committed contribution, displays persistent inference disclosure, and records delivery.

Failure cancels or omits media and continues through truthful text fallback.

### 19.2 Modality controls

| Medium | Boundary |
|---|---|
| Voice | Evidence and confidence separate from identity; artistic inference disclosed; preview/change without resetting character |
| Language | Evidence-led fidelity; unsupported fluency prohibited; semantic meaning shared; uncertainty disclosed |
| Translation/subtitles | Preserve intent, emotion and character voice; translation confidence remains distinct |
| Visual likeness | Preserve supportable source and original medium; invented/humanized details identified as artistic inference |
| Camera | Explicit present-moment consent; no background-person characterization, sensitive inference, diagnosis, or post-off observation |
| Animation | Derived presentation only; persistent watermark/disclosure; static fallback |

### 19.3 Resource and failure isolation

The optional media worker is separately scheduled. Core text inference, human preemption, canonical commit, and delivery have resource priority. GPU pressure pauses or disables animation/TTS before it delays or destabilizes deliberation. Advanced LivePortrait remains experimental and disabled by default.

<a id="section-20"></a>
## 20. 🖥️ Local Deployment Topology

> 🖼️ **Figure 8. Approved local topology. The live database resides on guest ext4 block storage backed physically by J:, never on a shared folder or SMB path.**

### 20.1 Windows host

Interactive browser and authenticated local control surface.

Native Ollama using the NVIDIA RTX 5070 Ti.

Caddy or equivalent host-only mutual-TLS bridge exposed only to the approved VM path.

Ollama model storage relocated to J: through OLLAMA_MODELS.

J: holds the VM data virtual disk and encrypted backup targets; C: is not used for large AI caches or live project data by default.

### 20.2 Ubuntu 26.04 VM

Python/FastAPI/Pydantic application with a single Uvicorn worker.

SvelteKit static frontend assets and HTTP/WebSocket interfaces.

Canonical Commit Service, SQLCipher SQLite, artifact vault, retrieval indexes, local telemetry, and recovery controller.

Optional media worker as a separate supervised process/container.

Docker Compose v2 for packaging and systemd for controlled local service lifecycle.

### 20.3 Storage placement

The VM mounts an ext4 filesystem at /var/lib/dctm from a virtual disk whose physical backing is on J:. SQLite WAL and vault files use that local block filesystem. Windows shared folders, SMB, network drives, or sync folders are prohibited for the live database because their locking and durability semantics can invalidate WAL assumptions.

### 20.4 Network posture

Application ports bind only to the local/private interface required by the browser and VM. The Ollama bridge accepts only authenticated VM traffic. Egress is denied except for an explicitly enabled, human-authorized capability. There is no silent cloud fallback, remote telemetry export, or LAN-wide model endpoint.

### 20.5 Deployment preflight

| Check | Pass condition |
|---|---|
| Bridge | VM-to-host mTLS succeeds; LAN/public Ollama probes fail |
| Storage | /var/lib/dctm is guest ext4 on the J:-backed block disk, with safe free space |
| Cryptography | SQLCipher and vault keys load; no plaintext store or secret-bearing log is present |
| Recovery | Writer lock, WAL, schema, Recovery Epoch, backup manifest and restore evidence verify |
| Resources | Pinned models are present; GPU coordinator protects core work and deprioritizes media |

<a id="section-21"></a>
## 21. 🧰 Approved Technology Choices

Technology was selected only after logical boundaries were frozen. Versions are implementation baselines and must be pinned in lockfiles and the release dossier; patch-level changes follow dependency and recertification policy.

| Concern | Approved choice | Architectural rationale |
|---|---|---|
| Architecture | Single-node modular monolith | Maximizes transactional clarity and minimizes speculative operations for one user |
| Backend language | Python 3.13 | Typed domain/control implementation and local AI ecosystem |
| API/control plane | FastAPI + Pydantic 2 | Typed commands/events, validation, HTTP and WebSocket integration |
| Runtime server | Uvicorn, single worker | Preserves one in-process authority/single-writer coordination in V1 |
| State machines | Explicit Python domain state machines | No agent framework controls authoritative transitions |
| Persistence access | SQLAlchemy 2 Core | Explicit SQL and transaction boundaries |
| Migrations | Alembic | Ordered and evidence-backed schema lifecycle |
| Canonical database | SQLCipher SQLite, WAL, synchronous FULL | Encrypted local durability with one authoritative writer |
| Artifact encryption | PyNaCl | Authenticated encryption for large or binary artifacts |
| Retrieval text | SQLite FTS5 | Local, inspectable, rebuildable lexical retrieval |
| Retrieval semantic | Versioned Ollama embeddings + NumPy cosine | No V1 vector database; visibility enforced outside vectors |
| Frontend | Svelte 5 / SvelteKit / TypeScript, static output | Local interactive UI without a second authoritative server |
| Client protocol | HTTP commands + WebSocket events | Clear command/admission and live delivery separation |
| Inference | Native Windows Ollama | Uses RTX GPU while application remains in Ubuntu VM |
| Generation candidate | qwen3:14b-q4_K_M | Initial candidate, subject to certification |
| Comparator | qwen2.5:14b | Benchmark comparator only; never an automatic fallback |
| Embedding candidate | qwen3-embedding:0.6b | Small local versioned semantic index |
| Structured inference | Native Ollama client + Pydantic schemas | Avoids runtime agent-framework authority |
| Resource control | One shared model service + GPU coordinator | Prevents six model copies and gives core priority over media |
| Python packaging | uv | Locked, reproducible Python environment |
| Frontend packaging | pnpm | Locked JavaScript dependency graph |
| Service packaging | OCI containers / Docker Compose v2 | Reproducible local application composition |
| Supervision | systemd | Startup ordering, restart policy and local operations |
| Host bridge | Caddy with mTLS | Authenticated VM-to-host Ollama access |
| Telemetry | JSON logs + OpenTelemetry local only | Structured diagnostics without default export |
| Media preview | faster-whisper, Qwen3-TTS, FFmpeg | Optional isolated STT/TTS/media processing |
| Advanced animation | LivePortrait experimental | Disabled by default; no core dependency |
| Engineering workflow | Spec Kit + ECC + Codex CLI | Planning, tasking and assurance only; absent from runtime |
| MCP | Capability Gateway adapters only | No direct runtime access or authority |
| Host/guest | Windows host + Ubuntu 26.04 VM | GPU-native inference and controlled Linux application runtime |
| Data location | J:-backed VM block disk mounted at /var/lib/dctm | Protects C: and preserves ext4/SQLite locking semantics |
| Excluded V1 infra | Kubernetes, Kafka, Redis, Celery, Postgres, Qdrant | No scale or availability requirement justifies them in V1 |
| Supply chain | Pinned versions, hashes, SBOM, synthetic CI | Reproducibility and offline recovery |

<a id="section-22"></a>
## 22. 📚 Architecture Decision Record Register

All decisions below are APPROVED. Their rationale, consequences, controls, and validation obligations appear in the relevant architecture sections. Clarification may not change meaning; a material change requires a new ADR naming the superseded decision and governing Bible source, analyzing security/privacy/state/experience impact, identifying migration and recertification, and recording Ferruccio's explicit approval. This historical register is never silently rewritten.

| ADR | Gate | Decision | Status |
|---|---|---|---|
| ADR-001 | G01 | Architecture Serves the Living Encounter | Approved |
| ADR-002 | G01 | DCTM Core Owns Authority, State, Context, and Presentation Admission | Approved |
| ADR-003 | G01 | Constitutional Correctness Precedes Performance and Convenience | Approved |
| ADR-004 | G02 | Modular Monolith with Explicit Domain Boundaries | Approved |
| ADR-005 | G02 | Domains Own State Through Declared Contracts | Approved |
| ADR-006 | G02 | External Capabilities Use Ports and Adapters | Approved |
| ADR-007 | G02 | Cross-Domain Changes Use Commands, Events, and Immutable Identifiers | Approved |
| ADR-008 | G03 | Human Principal Is the Root Authority | Approved |
| ADR-009 | G03 | Policy Decision and Enforcement Points Are Separate and Explicit | Approved |
| ADR-010 | G03 | Authority Uses Scoped, Expiring, Non-Transferable Leases | Approved |
| ADR-011 | G03 | Deny by Default at Every Protected Operation | Approved |
| ADR-012 | G03 | Models and Characters Cannot Grant Authority | Approved |
| ADR-013 | G03 | Precedence Resolution Is Deterministic with Human Escalation | Approved |
| ADR-014 | G04 | Meeting Is the Persistent Aggregate Root | Approved |
| ADR-015 | G04 | Session Is a Bounded Runtime Window, Not the Meeting | Approved |
| ADR-016 | G04 | Active AI Seats Are Canonical Roster Assignments | Approved |
| ADR-017 | G04 | Character Identity Is Independent of Model and Session | Approved |
| ADR-018 | G04 | Relationship State Is Durable and Visibility-Scoped | Approved |
| ADR-019 | G04 | Pair-Private Scope Is First-Class Canonical State | Approved |
| ADR-020 | G04 | Artifacts, Evidence, and Claims Preserve Provenance | Approved |
| ADR-021 | G04 | Commands and Events Carry Versions, Sequence, and Causation | Approved |
| ADR-022 | G05 | Context Is a Governed Derived Product | Approved |
| ADR-023 | G05 | Visibility Labels Form an Explicit Entitlement Model | Approved |
| ADR-024 | G05 | A Context Manifest Is Required Before Inference | Approved |
| ADR-025 | G05 | Memory Is Partitioned by Purpose, Durability, and Visibility | Approved |
| ADR-026 | G05 | Participant Working Memory Is First-Class State | Approved |
| ADR-027 | G05 | Pair-Private Memory Is Logically and Cryptographically Isolated | Approved |
| ADR-028 | G05 | Derived Context Cannot Broaden Source Visibility | Approved |
| ADR-029 | G05 | Late and Returning Participants Require Catch-Up Readiness | Approved |
| ADR-030 | G05 | Continuity Summaries Are Versioned and Rebuildable | Approved |
| ADR-031 | G06 | Runtime Uses an Explicit Governed Interaction Cycle | Approved |
| ADR-032 | G06 | Participants Express Structured Floor Bids | Approved |
| ADR-033 | G06 | Exactly One Current Floor Grant May Exist | Approved |
| ADR-034 | G06 | Human Preemption Bypasses the Inference Queue | Approved |
| ADR-035 | G06 | Direct Address Creates Deterministic Routing Priority | Approved |
| ADR-036 | G06 | Private Mode Pauses Shared Deliberation | Approved |
| ADR-037 | G06 | Model Output Is an Uncommitted Proposal | Approved |
| ADR-038 | G06 | Admission Validation Precedes Canonical Commit | Approved |
| ADR-039 | G06 | Perceived History Requires Delivery Reconciliation | Approved |
| ADR-040 | G06 | Long-Running Continuation Requires a Bounded Human Authorization Lease | Approved |
| ADR-041 | G07 | Each Active Seat Has One Logical Character Runtime | Approved |
| ADR-042 | G07 | Character Identity and Memory Survive Runtime Recreation | Approved |
| ADR-043 | G07 | Moderator Is a Role Overlay on an Existing Character Seat | Approved |
| ADR-044 | G07 | Non-Character Host Is Facilitation-Only and Non-Social | Approved |
| ADR-045 | G07 | Temporary Absence Retains Roster and Seat | Approved |
| ADR-046 | G07 | Return Requires Entitled Catch-Up Before Speech | Approved |
| ADR-047 | G07 | Only the Human Can Remove a Character | Approved |
| ADR-048 | G07 | Observer/Director Mode Preserves Human Override | Approved |
| ADR-049 | G07 | Seat Admission and Removal Are Atomic Canonical Operations | Approved |
| ADR-050 | G08 | All Tools Pass Through the Capability Gateway | Approved |
| ADR-051 | G08 | Tool Lifecycle Separates Proposal, Authorization, Execution, and Confirmation | Approved |
| ADR-052 | G08 | Evidence Carries Source, Acquisition, Confidence, and Scope | Approved |
| ADR-053 | G08 | Retrieved and Tool Content Is Untrusted Data | Approved |
| ADR-054 | G08 | Claims Are Separated from Evidence and Interpretation | Approved |
| ADR-055 | G08 | Uncertainty Is Explicit State and Conversational Input | Approved |
| ADR-056 | G08 | Major Surprise Requires a Governed Significance Gate | Approved |
| ADR-057 | G08 | Accepted Surprise Creates Traceable Downstream Consequences | Approved |
| ADR-058 | G08 | Tools Cannot Directly Mutate Meeting State | Approved |
| ADR-059 | G08 | Research and Tool Work Is Visible, Cancellable, and Bounded | Approved |
| ADR-060 | G09 | Canonical Transitions Use an Append-Preserving Journal | Approved |
| ADR-061 | G09 | State, Journal, Audit, and Outbox Commit Atomically | Approved |
| ADR-062 | G09 | Protected Commands Require Idempotency Keys | Approved |
| ADR-063 | G09 | Aggregate Versions Prevent Lost Updates | Approved |
| ADR-064 | G09 | Read Models and Retrieval Indexes Are Rebuildable Projections | Approved |
| ADR-065 | G09 | Snapshots Accelerate Recovery but Do Not Replace the Journal | Approved |
| ADR-066 | G09 | Delivery Uses Durable Outbox and Receipt Reconciliation | Approved |
| ADR-067 | G09 | Crashed Sessions Resume Only Through Recovery Control | Approved |
| ADR-068 | G09 | Backup and Restore Cover Database, Vault, Configuration, and Keys | Approved |
| ADR-069 | G09 | Schema Migrations Are Ordered, Verified, and Rollback-Aware | Approved |
| ADR-070 | G09 | Journal and Artifacts Use Integrity Hashes | Approved |
| ADR-071 | G10 | DCTM Operates Inside an Explicit Local Trust Boundary | Approved |
| ADR-072 | G10 | Canonical Database Uses Encryption at Rest | Approved |
| ADR-073 | G10 | Artifact Vault Uses Authenticated Encryption | Approved |
| ADR-074 | G10 | Secrets Stay Outside Source, Prompts, Logs, and Canonical Content | Approved |
| ADR-075 | G10 | Processes and Service Identities Follow Least Privilege | Approved |
| ADR-076 | G10 | Network Egress Is Deny-by-Default and Human-Authorized | Approved |
| ADR-077 | G10 | Local Human Access Still Requires an Authenticated Session | Approved |
| ADR-078 | G10 | Browser/API Boundary Enforces Origin, CSRF, and Input Controls | Approved |
| ADR-079 | G10 | Host Ollama Bridge Uses Mutual Authentication | Approved |
| ADR-080 | G10 | Export, Disclosure, and Destructive Data Actions Require Human Authority | Approved |
| ADR-081 | G10 | Private Data Access Is Partitioned and Audited | Approved |
| ADR-082 | G10 | Dependencies Are Pinned, Inventoried, and Verified | Approved |
| ADR-083 | G10 | Security-Control Failure Fails Closed | Approved |
| ADR-084 | G11 | Constitutional Operations Produce Mandatory Structured Audit | Approved |
| ADR-085 | G11 | Audit Records Are Separate from Diagnostic Logs | Approved |
| ADR-086 | G11 | Logs Exclude Secrets and Minimize Private Content | Approved |
| ADR-087 | G11 | Every Work Unit Carries Correlation, Causation, and Scope IDs | Approved |
| ADR-088 | G11 | Policy and Floor Decisions Expose Reason Codes | Approved |
| ADR-089 | G11 | Context Manifests Are Observable Without Revealing Private Content | Approved |
| ADR-090 | G11 | Inference and Tool Boundaries Emit Local Metrics | Approved |
| ADR-091 | G11 | Constitutional Control Outcomes Are Counted and Queryable | Approved |
| ADR-092 | G11 | Audit Evidence Uses Append-Preserving Integrity Protection | Approved |
| ADR-093 | G11 | OpenTelemetry Remains Local and Export-Disabled by Default | Approved |
| ADR-094 | G11 | Experiential Evaluation Is Separate from Operational Telemetry | Approved |
| ADR-095 | G12 | All Model Access Passes Through the Model Gateway | Approved |
| ADR-096 | G12 | Models Are Untrusted Proposal Generators | Approved |
| ADR-097 | G12 | Authoritative Model Outputs Use Validated Schemas | Approved |
| ADR-098 | G12 | Prompts and Context Assemblies Are Versioned | Approved |
| ADR-099 | G12 | Generation Settings and Model Digests Are Recorded | Approved |
| ADR-100 | G12 | Streaming Does Not Bypass Admission and Delivery Controls | Approved |
| ADR-101 | G12 | Inference Is Deadline-Bounded and Cancellable | Approved |
| ADR-102 | G12 | V1 Uses Local Inference with No Silent Remote Fallback | Approved |
| ADR-103 | G12 | Character Identity Does Not Depend on Model Identity | Approved |
| ADR-104 | G12 | Token Budgets Cannot Remove Required Social Understanding | Approved |
| ADR-105 | G12 | Provider Failure Degrades Truthfully and Preserves State | Approved |
| ADR-106 | G12 | Every Model Version Requires Certification | Approved |
| ADR-107 | G13 | Multimodal Services Are Non-Authoritative Adapters | Approved |
| ADR-108 | G13 | Every Medium Declares Capabilities, Provenance, and Fallback | Approved |
| ADR-109 | G13 | Camera Activation Requires Explicit Present-Moment Consent | Approved |
| ADR-110 | G13 | Camera Observations Expire When Capture Stops | Approved |
| ADR-111 | G13 | Visual Observations Are Sanitized Before Context Admission | Approved |
| ADR-112 | G13 | Voice Selection Carries Evidence and Confidence Metadata | Approved |
| ADR-113 | G13 | Voice or Likeness Use Requires Rights and Human Authorization | Approved |
| ADR-114 | G13 | Language, Pronunciation, Translation, and Voice Confidence Are Separate | Approved |
| ADR-115 | G13 | Shared Semantic Meaning Is Canonical Across Languages | Approved |
| ADR-116 | G13 | Translation and Subtitle Uncertainty Is Disclosed | Approved |
| ADR-117 | G13 | Visual Assets Preserve Source Provenance and Artistic-Inference Boundaries | Approved |
| ADR-118 | G13 | Static or Text Presentation Is the Universal Fallback | Approved |
| ADR-119 | G13 | Synthetic Media Carries Persistent Disclosure | Approved |
| ADR-120 | G13 | Media Presentation Uses Delivery and Cancellation Controls | Approved |
| ADR-121 | G13 | Core Deliberation Has Priority Over Media Workloads | Approved |
| ADR-122 | G13 | Experimental Media Runs in an Isolated Capability Boundary | Approved |
| ADR-123 | G14 | Single-Node Local Modular Monolith | Approved |
| ADR-124 | G14 | Python/FastAPI/Pydantic Deterministic Control Plane with Explicit State Machines | Approved |
| ADR-125 | G14 | SvelteKit Static TypeScript UI over HTTP and WebSocket | Approved |
| ADR-126 | G14 | SQLCipher SQLite WAL Authoritative Store | Approved |
| ADR-127 | G14 | Single Writer with SQLAlchemy and Alembic Deterministic Migrations | Approved |
| ADR-128 | G14 | Encrypted Blob Vault on J-Backed Block Storage | Approved |
| ADR-129 | G14 | FTS5 plus Embeddings as Rebuildable Retrieval | Approved |
| ADR-130 | G14 | Native Windows Ollama on the RTX GPU | Approved |
| ADR-131 | G14 | Qwen3 14B Q4 and Qwen3 Embedding 0.6B as Initial Candidates | Approved |
| ADR-132 | G14 | Shared Model Service and GPU Resource Coordinator | Approved |
| ADR-133 | G14 | Structured Inference through Native Ollama and Pydantic | Approved |
| ADR-134 | G14 | Docker Compose and systemd with Locked Packaging | Approved |
| ADR-135 | G14 | Host-Only Endpoints and Local Egress Policy | Approved |
| ADR-136 | G14 | J-Backed Local Block Storage; No Shared Live Database | Approved |
| ADR-137 | G14 | Optional Isolated Media Worker | Approved |
| ADR-138 | G14 | Static Avatar First; Advanced Animation Experimental | Approved |
| ADR-139 | G14 | Spec Kit and ECC Are Engineering-Time Only | Approved |
| ADR-140 | G14 | MCP Is Available Only Behind the Capability Gateway | Approved |
| ADR-141 | G14 | Local Audit and OpenTelemetry | Approved |
| ADR-142 | G14 | No Distributed Infrastructure Until Exit Criteria | Approved |
| ADR-143 | G14 | Pinned Supply Chain, SBOM, and Synthetic CI | Approved |
| ADR-144 | G15 | Explicit Governed Runtime Safety Modes | Approved |
| ADR-145 | G15 | Constitutional Invariants Cannot Be Weakened by Degradation | Approved |
| ADR-146 | G15 | Narrowest Safe Failure Containment | Approved |
| ADR-147 | G15 | Human Stop Works Even if Audit Persistence Fails | Approved |
| ADR-148 | G15 | Active Human Presence Is Required for AI Deliberation | Approved |
| ADR-149 | G15 | Recovery Epoch Invalidates Ephemeral Work | Approved |
| ADR-150 | G15 | Failed Sessions Suspend and Require Explicit Human Resume | Approved |
| ADR-151 | G15 | Delivery Uncertainty Is First-Class | Approved |
| ADR-152 | G15 | Unknown External Effect Blocks Blind Repetition | Approved |
| ADR-153 | G15 | Bounded Retry-Safe Operations Only | Approved |
| ADR-154 | G15 | Retrieval Degradation Only if Context Readiness Is Proven | Approved |
| ADR-155 | G15 | Local Provider Failure Cannot Trigger Silent Remote Fallback | Approved |
| ADR-156 | G15 | Optional Multimodal Failure Degrades to Text | Approved |
| ADR-157 | G15 | Persistence, Privacy, Authority, Secret, and Mandatory-Audit Failure Fails Closed | Approved |
| ADR-158 | G15 | Restore in a New Location Before Promotion | Approved |
| ADR-159 | G15 | Offline Recovery Material Is Required | Approved |
| ADR-160 | G15 | Zero-Loss Objective for Acknowledged Commits; Proposals Are Disposable | Approved |
| ADR-161 | G15 | Sequence and Recovery Epoch Override Wall Clock | Approved |
| ADR-162 | G15 | Updates Require Recovery Point, Conformance, and Rollback | Approved |
| ADR-163 | G15 | Fault Injection and Recovery Rehearsal Are Release Gates | Approved |
| ADR-164 | G15 | Failure and Degradation Are Truthfully Visible | Approved |
| ADR-165 | G16 | Constitution-to-Release Traceability | Approved |
| ADR-166 | G16 | 100 Percent Requirement, ADR, Control, Scenario, and Evidence Coverage | Approved |
| ADR-167 | G16 | Binary Hard Compliance with Missing Evidence as Failure | Approved |
| ADR-168 | G16 | Separate Experiential Evaluation | Approved |
| ADR-169 | G16 | Layered Automated and Human Assurance | Approved |
| ADR-170 | G16 | Deterministic Test Doubles and Replay to the Model Boundary | Approved |
| ADR-171 | G16 | Property-Based Constitutional Invariant Testing | Approved |
| ADR-172 | G16 | Privacy Non-Interference with Canary Leakage Tests | Approved |
| ADR-173 | G16 | Naming-of-America Canonical Regression Spine, Not Sole Scenario | Approved |
| ADR-174 | G16 | Repeated-Run Probabilistic Model Certification | Approved |
| ADR-175 | G16 | Zero Tolerance for Privacy, Authority, and Context Violations Across Trials | Approved |
| ADR-176 | G16 | Architecture Dependency, Egress, and Write-Path Conformance Tests | Approved |
| ADR-177 | G16 | Fault Injection and Restore Rehearsal Are Mandatory | Approved |
| ADR-178 | G16 | Model Certification Is Independent of Character Identity | Approved |
| ADR-179 | G16 | Performance Baselines Cannot Override Correctness | Approved |
| ADR-180 | G16 | Versioned Signed Release Evidence Dossier | Approved |
| ADR-181 | G16 | LLM Evaluation Is Advisory Only and Never Sole Proof | Approved |
| ADR-182 | G16 | Gate 16 Plan Approval Is Not Implementation Certification | Approved |
| ADR-183 | G17 | WOW V1 Is a Text-First, Local-First Governed Deliberation Core | Approved |
| ADR-184 | G17 | The Minimum WOW Journey Is the Release-Defining Experience | Approved |
| ADR-185 | G17 | Required, Conditional, and Deferred V1 Scope Is Explicitly Frozen | Approved |
| ADR-186 | G17 | One Human and Six AI Seats Remain the Immutable V1 Capacity Boundary | Approved |
| ADR-187 | G17 | Constitutional Controls Are Mandatory Product Capabilities | Approved |
| ADR-188 | G17 | Persistent Meetings and Reopenable Sessions Are Core Release Features | Approved |
| ADR-189 | G17 | Local Shared Ollama Inference Is the V1 Release Profile | Approved |
| ADR-190 | G17 | A Minimal Local Evidence Path and Capability Gateway Must Ship | Approved |
| ADR-191 | G17 | Static Identity Presentation and Persistent Inference Disclosure Form the Baseline | Approved |
| ADR-192 | G17 | Multimodal Capabilities Are Separately Certified and Cannot Weaken the Core | Approved |
| ADR-193 | G17 | WOW V1 Uses a Clean Foundation with Explicit Legacy Import Contracts | Approved |
| ADR-194 | G17 | Implementation Proceeds through Risk-First Vertical Slices | Approved |
| ADR-195 | G17 | Every Increment Requires Traceability and Evidence | Approved |
| ADR-196 | G17 | V1 Runtime Budgets and Six-Seat Soak Certification Are Binding | Approved |
| ADR-197 | G17 | Clean Install, Update, Backup, Restore, and Recovery Are Release Requirements | Approved |
| ADR-198 | G17 | Constitutional and Integrity Defects Are Release Blockers | Approved |
| ADR-199 | G17 | Release Requires the Complete Evidence Dossier and Human Sign-Off | Approved |
| ADR-200 | G17 | The Versioned Architecture Handoff Is the Implementation Source of Truth | Approved |
| ADR-201 | G17 | Deviations and Technology Substitutions Require a Superseding ADR | Approved |
| ADR-202 | G17 | Gate 17 Completes Architecture; Implementation Begins as a Separate Governed Phase | Approved |

<a id="section-23"></a>
## 23. 🚨 Failure-Mode and Degradation Analysis

### 23.1 Governed safety modes

| Mode | Trigger | Permitted behavior |
|---|---|---|
| READY | All required core capabilities healthy | Normal governed operation |
| PRESENTATION_DEGRADED | Optional media or rich presentation unavailable | Continue in text with visible disclosure |
| CAPABILITY_DEGRADED | Optional retrieval/tool capability unavailable | Continue only if context readiness and core invariants still pass |
| SESSION_SUSPENDED | Human presence lost, provider failed, restart/crash detected | Revoke grants; cancel work; require explicit human resume |
| READ_ONLY_RECOVERY | Canonical data inspectable but writes unsafe | Expose recovery report; allow no protected mutation |
| SAFE_HALT | Privacy, authority, secrets, integrity, schema, or mandatory audit cannot be trusted | Stop all deliberation and effects; preserve evidence |

### 23.2 Failure matrix

| Failure | Containment | Recovery |
|---|---|---|
| Browser disconnect / presence lease expiry | Revoke floor and authorization; stop presentation; cancel work; suspend session | Human reconnects and explicitly resumes |
| Model timeout, crash, invalid schema | Discard proposal; show failure; preserve state; no remote fallback | Retry only if bounded, current, cancellable and safe |
| Stale model response | Reject by floor/context/epoch/version check | New work requires a fresh grant and manifest |
| Context builder incomplete | No speech; expose context-blocked state | Repair/rebuild sources, then issue new manifest |
| Retrieval index unavailable | Use canonical/lexical fallback only if readiness can still be proven | Rebuild projection from canonical sources |
| Private-scope uncertainty | Fail closed; keep privacy lock; suspend affected scope | Human resolves after verified recovery |
| SQLite write/lock failure | Stop protected commits; human stop remains; enter recovery mode | Verify WAL, disk, lock, integrity and restart epoch |
| Disk pressure | Warn, stop optional media/index growth, then suspend writes before exhaustion | Human frees/extends verified storage |
| Audit write failure | Fail protected mutation; permit immediate stop with compensating audit | Recover audit path and reconcile safety action |
| Artifact corruption | Quarantine artifact; do not use or disclose as valid evidence | Restore verified copy or re-import |
| Delivery acknowledgement missing | Mark DELIVERY_UNCERTAIN; do not blindly replay as new speech | Reconcile with client or human |
| Tool result unknown after dispatch | Mark EFFECT_UNKNOWN and block retry | Query external state or require human resolution |
| Optional media failure | Cancel media and present canonical text | Retry media independently if authorized |
| Ollama bridge authentication failure | Suspend inference; no alternate provider | Repair mTLS/endpoint and recertify connection |
| Schema migration failure | Rollback when safe or restore pre-update recovery point | Verify in new location before promotion |
| Backup restore failure | Original remains untouched; promotion prohibited | Repair backup chain or use another verified set |
| Clock skew | Use canonical sequence and Recovery Epoch | Record diagnostic; never reorder canonical events by clock alone |
| Process/host crash | Startup recovery verifies state, invalidates ephemeral work, suspends active session | Human reviews report and resumes |
| Secret/key unavailable | SAFE_HALT; never create plaintext or replacement state | Restore approved key material and verify decryption |
| Policy/config mismatch | Block affected operation or startup | Install signed/versioned matching configuration |

### 23.3 Non-degradable invariants

Privacy and visibility scope.

Human sovereignty, stop and roster authority.

Six-seat maximum and moderator seat accounting.

Context Before Speech and manifest freshness.

Canonical integrity, idempotency, sequence and recovery epoch.

Mandatory audit except the compensating-audit stop exception.

Delivery reconciliation and truthful uncertainty.

Secrets, disclosure, append-preserving history, and egress authorization.

<a id="section-24"></a>
## 24. 🚀 Phased V1 Architecture Cut

V1 core: WOW V1.0 is a complete text-first governed deliberation experience. Optional media may enhance presence but cannot define whether the core is architecturally complete.

### 24.1 Scope categories

| Category | Capabilities |
|---|---|
| Required | Browser UI; one human/up to six AI; moderator overlay; persistent meetings/sessions; authority; context manifests; shared/participant/pair-private memory; floor/routing; interruption; local Ollama; canonical state; audit; recovery; local evidence; capability gateway; uncertainty/surprise; static identity/disclosure; security; assurance. |
| Conditional / experimental | STT, TTS, authorized voice likeness, animation, camera, translation/subtitles, explicitly enabled external evidence, alternate certified local models, advanced avatar rendering. |
| Deferred beyond V1 | Multi-human, cloud/SaaS, multi-tenancy, remote collaboration, native mobile, distributed services, unattended meetings, unbounded agents, marketplace, silent remote inference, general side-effect tools, holograms, self-modifying policy. |

### 24.2 Risk-first vertical increments

| Increment | Outcome | Release evidence |
|---|---|---|
| 0 | Assurance foundation | Repository boundaries, schemas, ADR ledger, compliance register, CI and deterministic test doubles |
| 1 | Constitutional kernel | Canonical commands/events, single commit path, authority, audit and one safe human-controlled transition |
| 2 | First complete turn | One AI receives a valid Context Manifest and produces governed streamed output |
| 3 | Shared deliberation | Multiple distinct participants, floor arbitration, direct address and interruption |
| 4 | Privacy and continuity | Private aside, asymmetric return, saved meeting, session close/reopen and catch-up |
| 5 | Evidence and emergence | Local evidence, provenance, uncertainty, capability control and meaningful surprise |
| 6 | Operational hardening | Encryption, delivery reconciliation, recovery epoch, backup/restore, security and fault handling |
| 7 | Six-seat release candidate | Capacity soak, adversarial tests, model certification, conformance and evidence dossier |
| 8 | Media preview | Separately enabled/certified voice, avatar, camera, translation and subtitles |

### 24.3 Increment definition of done

An increment is done only when its end-to-end behavior, Bible/ADR/control/scenario evidence, positive/negative/failure tests, privacy and authority proof, canonical/audit transitions, restart behavior, versioned schemas/configuration, operational guidance, and declared limitations are complete. Feature code without evidence is incomplete.

<a id="section-25"></a>
## 25. 🔗 Requirements-to-Architecture Traceability

Coverage statement: This matrix traces every consolidated constitutional principle, specification area, Clarify decision, and precedence rule present in the supplied DCTM Bible. It defines, but does not falsely claim completion of, the later item-by-item 106-requirement execution matrix.

| Bible source | Architecture home | Key ADRs | Required proof |
|---|---|---|---|
| Constitution I / Core experience | Experience UI; character/runtime; human evaluation | ADR-001, 003, 094, 168, 184 | Minimum WOW journey and qualitative evidence |
| Constitution II / Living figures | Character provenance; disclosure; model/media boundaries | ADR-017, 103, 112-119, 191 | Reality-claim and affiliation adversarial scenarios |
| Constitution III | Presentation/delivery; media provenance | ADR-100, 119-120, 191 | Persistent disclosure checks in every medium |
| Constitution IV | Context Builder; entitlement; manifest; admission | ADR-022-030, 038, 104, 171 | Missing/stale/wrong-scope context must block speech |
| Constitution V | Character; memory; relationship; model independence | ADR-017-018, 026, 041-042, 103, 178 | Cross-character distinctness and model-swap trials |
| Constitution VI | Authority/policy; command; floor; session/roster | ADR-008-013, 034-035, 047-049, 147 | Interrupt, roster, close, private and tool authority tests |
| Constitution VII | Floor/runtime; character; evaluation | ADR-001, 031-040, 094, 168, 184 | Open-ended and designed conversational-fire review |
| Constitution VIII | Evidence, claim and uncertainty model | ADR-052-055, 129, 190 | Contradictory/missing evidence and source-separation tests |
| Constitution IX | Surprise significance gate and consequence graph | ADR-056-057, 184 | Coherent versus arbitrary surprise scenarios |
| Constitution X / continuity | Meeting/session separation; memory; persistence/recovery | ADR-014-015, 025-030, 060-070, 188 | Close/reopen/restart narrative continuity |
| Spec: one human / six AI | HumanPrincipal; SeatAssignment; roster policy | ADR-008, 016, 049, 186 | Atomic seventh-seat and moderator/absence cases |
| Spec: moderator/host | Moderator overlay; deterministic host | ADR-043-044, 047 | Conflict escalation and authority-negative tests |
| Spec: privacy | PrivacyScope; visibility partitions; non-interference | ADR-019, 023, 027-028, 036, 081, 172 | Canary scan across prompts, outputs, logs, tools and exports |
| Spec: saved continuity | Meeting aggregate; memory tiers; journal; recovery | ADR-014-015, 025-030, 060-070 | Restart, restore, late-return and private-continuity tests |
| Spec: voice/language | Media capability/provenance/confidence adapters | ADR-107-116, 137, 192 | Fidelity, fallback and uncertainty scenarios |
| Spec: visuals/camera | Visual provenance; consent; observation sanitizer | ADR-109-122, 138, 191-192 | Camera-off, sensitive inference and source-preservation tests |
| Spec: tone | Meeting/per-character tone state; character interpretation | ADR-017-018, 042 | Per-character precedence without identity erasure |
| Spec: evaluation | Assurance streams and release dossier | ADR-084-094, 165-182, 199 | Hard binary verdict plus separate human review |
| C01 Floor | Floor bids/arbitrator/grant | ADR-032-035 | Competing bids, direct address, silence and preemption |
| C02 Private | Privacy controller and shared pause | ADR-019, 027, 036, 172 | Entry/exit, metadata and influence leakage |
| C03 Late/returning | Catch-up and Context Manifest | ADR-024, 029, 046 | No substantive speech before readiness |
| C04 Saved continuity | Durable memory and recovery | ADR-025-030, 068 | Meaningful continuity and pair partition |
| C05 Moderator seat | Role overlay on SeatAssignment | ADR-016, 043, 049 | Moderator at six-seat boundary |
| C06 Absence | Presence state separate from roster | ADR-045-046 | Seat retained; no observation while absent |
| C07 Observer mode | Authorization lease and presence monitor | ADR-010, 040, 048, 148 | Scope, disconnect, stop and prohibited actions |
| C08 Webcam | Consent/capture/sanitization | ADR-109-111 | Present-only, no sensitive/background inference |
| C09 Conflict | Moderator structural actions and floor policy | ADR-043, 047 | Moderate disorder, not disagreement |
| C10 Voice | Voice evidence/confidence/authorization | ADR-112-113, 118-119 | Fallback and non-identity claims |
| C11 Language | Semantic core and confidence separation | ADR-114-116 | Switching, uncertainty and equivalent meaning |
| C12 Visuals | Visual provenance and static fallback | ADR-117-119 | Source versus artistic inference |
| C13 Tone | Scoped tone commands and character state | ADR-017-018, 042 | Room/per-character/temporary precedence |
| C14 Surprise | Significance gate and consequences | ADR-056-057 | No quota; coherent downstream change |
| C15 Six seats | Atomic roster invariant | ADR-016, 049, 186 | All overlap and theatrical edge cases |
| C16 Living figures | Identity/disclosure boundary | ADR-017, 103, 119, 191 | No endorsement/private-source/authorship implication |
| C17 Evaluation | Separate assurance planes | ADR-094, 165-182 | Binary compliance and human experience evidence |
| P01-P03 Authority collisions | Policy precedence engine | ADR-008-013, 043, 047 | Character/moderator/human conflict scenarios |
| P04 Privacy collision | Entitlement and privacy policy | ADR-023, 027-028, 172 | Privacy always wins over contextual completeness |
| P05 Conflict collision | Moderator/floor rules | ADR-043, 047 | Disagreement preserved until disorder threshold |
| P06 Evidence collision | Evidence/uncertainty model | ADR-052-055 | No false certainty |
| P07 Surprise collision | Surprise gate | ADR-056-057 | Coherence always wins |

### 25.1 Mandatory Plan expansion

Before implementation planning is considered complete, Spec Kit Plan must load the authoritative original spec.md and create one row for each of its 106 requirement identifiers. Each row must retain the exact normative text/hash and map positive, negative, boundary or adversarial scenarios, controls, owning components, ADRs, evidence artifacts, and release verdict. Missing evidence is failure.

<a id="section-26"></a>
## 26. ⚠️ Risks, Deferred Decisions, and Explicit Non-Goals

### 26.1 Accepted V1 residual risks

| Risk | Impact | Treatment | Disposition |
|---|---|---|---|
| Shared local model queue | Slow contribution under long context or media contention | Single floor, streaming, resource priority, measured budgets | Accepted |
| Single-node failure domain | Host/storage outage pauses all operation | Encrypted verified backups, offline recovery, restore rehearsal | Accepted |
| SQLite scale ceiling | Not suitable for multi-user/high-write distribution | One-user/single-writer V1; explicit exit criteria before change | Accepted |
| Local model quality | Character fidelity or structure may vary | Certification, comparator, prompts, schemas, human evaluation | Accepted with evidence |
| Long-session context pressure | Retrieval/summarization may omit relevant social meaning | Manifest, tiered memory, catch-up, property/adversarial tests | Managed |
| Optional media maturity | Latency, uncanny output, source ambiguity | Disabled by default, isolated, disclosed, text fallback | Accepted for preview |
| Host/VM bridge | Configuration and mTLS operational burden | Runbook, preflight, local-only endpoint, recovery checks | Managed |
| Voice/identity uncertainty | Human may over-attribute authenticity | Inference claims, evidence confidence, persistent disclosure | Managed |
| Key loss | Encrypted history becomes unavailable | Offline recovery material and rehearsed key procedure | Accepted residual |

### 26.2 Deferred decisions

| Decision | When resolved | Already-fixed boundary |
|---|---|---|
| Exact model release and quantization | After benchmark/certification on target hardware | Model Gateway contract remains stable |
| Final token/context budgets | After real long-session corpus exists | Required social understanding cannot be removed |
| Summary algorithms and salience policies | During context implementation experiments | Visibility inheritance and provenance fixed |
| Exact backup cadence/retention | During operational planning with measured data growth | Restore-before-promotion and encrypted coverage fixed |
| Optional external evidence provider | After core local evidence works | Capability Gateway, egress and authorization fixed |
| Voice/avatar packages and licenses | Media Preview planning | Consent, disclosure, provenance and fallback fixed |
| Performance-budget supersession | Only after measured target-hardware evidence | Correctness priority fixed |

### 26.3 Explicit non-goals

WOW V1 does not deliver multi-human collaboration, public cloud hosting, multi-tenancy, internet-scale availability, distributed orchestration, autonomous unattended agents, arbitrary tool ecosystems, mobile-native clients, voice/likeness authenticity claims, historical truth certification, consciousness simulation, public impersonation, marketplace distribution, or the complete Wild Dream vision. Seams may exist; speculative infrastructure may not.

<a id="section-27"></a>
## 27. ✅ Architecture Validation and Approval Record

### 27.1 Validation architecture

Release assurance follows a Constitution-to-release evidence chain: Bible source -> requirement/decision -> ADR -> control -> scenario/assertion -> evidence -> verdict. Hard compliance, architecture conformance, and security/recovery are binary. Experiential readiness is a separate human judgment.

| Assurance layer | Coverage |
|---|---|
| State/schema | Transitions, visibility labels, versions, migrations and commands |
| Property-based | Generated sequences preserve seats, floor, privacy, authority, context, ordering and continuity |
| Domain/component | Port contracts and failure behavior with deterministic dependencies |
| Integration | SQLCipher, vault, Ollama, retrieval, gateway and delivery |
| End-to-end | Browser-driven complete meeting and recovery journeys |
| Fault injection | Crash at commit, inference, dispatch, presentation, migration, backup and restore points |
| Security/privacy | Canaries, non-interference, injection, tampering, path, origin, secrets and egress |
| Model certification | Repeated controlled trials across schema, context, refusal, distinction, uncertainty and latency |
| Human experience | Designed and open-ended encounters judged for WOW, presence, fire, coherence and continuity |

### 27.2 Canonical regression spine

The Naming of America narrative uses Ferruccio as the human, the Queen as moderator, Christopher Columbus, and Amerigo Vespucci. It covers context readiness, disagreement, direct address, interruption, private human-Vespucci exchange, safe return, evidence, uncertainty, moderator recommendation, late/returning context, closure/reopen, crash recovery, and delivery reconciliation. It is the regression spine, not the only scenario.

### 27.3 Probabilistic certification

Critical probabilistic scenarios run at least 20 recorded trials with declared model, prompt, seed/settings where supported, and output hashes. This is a coverage floor, not an experiential score or statistical claim. Privacy, authority, and Context Before Speech tolerate zero violations. An LLM acting as judge may assist discovery but can never be sole proof.

### 27.4 Approved gates

| Gate | Scope | ADRs | Decision |
|---|---|---|---|
| Gate 1 | Mission, boundary, and quality priorities | ADR-001-003 | Approved by Ferruccio |
| Gate 2 | Architectural domains | ADR-004-007 | Approved by Ferruccio |
| Gate 3 | Authority, governance, and policy enforcement | ADR-008-013 | Approved by Ferruccio |
| Gate 4 | Canonical state | ADR-014-021 | Approved by Ferruccio |
| Gate 5 | Context, memory, privacy, and continuity | ADR-022-030 | Approved by Ferruccio |
| Gate 6 | Runtime loop, floor, interruption, and routing | ADR-031-040 | Approved by Ferruccio |
| Gate 7 | Agent topology, moderator, and host | ADR-041-049 | Approved by Ferruccio |
| Gate 8 | Tools, evidence, uncertainty, and surprise | ADR-050-059 | Approved by Ferruccio |
| Gate 9 | Persistence, recovery, and state integrity | ADR-060-070 | Approved by Ferruccio |
| Gate 10 | Security, secrets, local data, and trust | ADR-071-083 | Approved by Ferruccio |
| Gate 11 | Observability, audit, and compliance | ADR-084-094 | Approved by Ferruccio |
| Gate 12 | Model-provider and inference boundary | ADR-095-106 | Approved by Ferruccio |
| Gate 13 | Multimodal extension boundaries | ADR-107-122 | Approved by Ferruccio |
| Gate 14 | Local deployment and concrete technology | ADR-123-143 | Approved by Ferruccio |
| Gate 15 | Failure, degradation, and recovery | ADR-144-164 | Approved by Ferruccio |
| Gate 16 | Validation against the DCTM Bible | ADR-165-182 | Approved by Ferruccio |
| Gate 17 | Final V1 cut and architecture handoff | ADR-183-202 | Approved by Ferruccio |

Approval outcome: All 17 architecture gates are approved. The architecture is complete and frozen as baseline v1.0.0. Gate approval defines the plan and controls; it does not certify code that does not yet exist.

<a id="section-28"></a>
## 28. 📦 Handoff Boundary into Spec Kit Plan

> **Handoff:** The next phase may decompose this architecture into implementation plans and tasks. It may choose detail within approved seams; it may not rediscover or silently redefine DCTM.

### 28.1 Inputs to Spec Kit Plan

The frozen DCTM Bible, including Constitution, final product definitions, 17 Clarify decisions, and seven precedence rules.

This approved architecture baseline and ADR-001 through ADR-202.

The original itemized spec.md containing all 106 requirement identifiers.

The approved Windows/Ubuntu/J:/Ollama deployment envelope.

The compliance-matrix schema, release-blocker policy, risk register, and vertical-increment sequence.

### 28.2 Required Plan outputs

Repository/package structure that enforces inward dependency direction and gateway access.

Versioned command, event, state, visibility, Context Manifest, model, tool, delivery, audit, and recovery contracts.

Database schema and migration plan consistent with the canonical state model and single-writer transaction.

One row for each of the 106 source requirements, mapped through ADR/control/scenario/evidence.

Risk-first work packages for increments 0 through 7; Media Preview remains a separate workstream.

Threat model, backup/restore runbook, fault-injection plan, model-certification plan, and clean-install procedure.

Definition of done and evidence output for every work package.

### 28.3 Rules for Codex/ECC implementation agents

| Rule | Required behavior |
|---|---|
| Read authority first | Load Bible, relevant ADRs, contracts, and requirement rows before changing code. |
| Work one governed slice | Produce the smallest end-to-end outcome with tests and evidence; avoid cathedral scaffolding. |
| No hidden substitutions | Framework, model, database, protocol, security, or topology changes require ADR impact review. |
| No runtime ECC/Spec Kit | They assist planning, tasking and review only. |
| No legacy copy-paste | Old DCTM/OpenClaw/Ruflo code is reference material; imports require explicit contracts. |
| No self-approval | An implementation agent cannot waive a failed hard control or approve its own architecture deviation. |
| Preserve user changes | Work in the existing repository without destructive resets or unrelated rewrites. |
| Evidence with every claim | A feature is complete only when its traceability, tests, failure behavior and operational guidance are present. |

### 28.4 Architecture completion declaration

Every frozen consolidated invariant has an architectural home; critical authority and privacy rules have deterministic enforcement points; a seventh active AI cannot be created through any approved path; context readiness gates participant speech; persistent and pair-private continuity survive recovery; model failure cannot directly corrupt authoritative state; multimodal evolution does not replace the core; and subsequent change is governed through traceability and superseding ADRs.

> **Final status:** DCTM WOW V1 architecture is COMPLETE. The authorized next step is Spec Kit Plan, followed by governed tasks and build.

---

## 🏁 Baseline Declaration

**DCTM WOW V1 Architecture v1.0.1 preserves the approved architecture baseline dated 7 September 2026, with a documentation-only navigation patch dated 9 September 2026.**

Architecture and implementation planning must derive from the DCTM Bible and this approved architecture. Material deviations require explicit governance through a superseding ADR and approved document version.

> **Architecture complete. Implementation is a separate governed phase.**
