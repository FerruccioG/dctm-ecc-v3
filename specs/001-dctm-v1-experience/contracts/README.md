# Versioned Contracts

The catalog defines planning-level contract obligations; implementation schemas will be versioned under `packages/dctm/domain/contracts/`. Compatibility is explicit: additive optional fields may preserve a major version; changed meaning, authority, visibility, or invariant requires a new version and, where material, a superseding ADR. Unknown versions fail closed.

All protected envelopes include `schema_version`, immutable command/event ID, meeting/session/scope identifiers as applicable, correlation/causation IDs, idempotency key, expected aggregate version, policy version, and Recovery Epoch. Content-bearing fields carry visibility/provenance references. See [v1-contract-catalog.md](v1-contract-catalog.md).
