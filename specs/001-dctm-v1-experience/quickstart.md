# Quickstart: Validate Sprint 0.2 / Sprint 1 Readiness

This validates planning artifacts only; it does not run DCTM features.

## Prerequisites

- Repository on branch `main`, matching the frozen V1 specification.
- Certified Gate Zero toolchain; do not upgrade it.
- Frozen Bible, Architecture v1.0.1, and spec present at their recorded paths.

## Checks

```bash
test ! -e specs/001-dctm-v1-experience/tasks.md

test "$(grep -Ec '^[|] FR-[0-9]{3} [|]' specs/001-dctm-v1-experience/compliance-register.md)" -eq 106

test "$(grep -Ec '^[|] SC-[0-9]{3} [|]' specs/001-dctm-v1-experience/success-criteria-register.md)" -eq 20

test "$(grep -oE 'ADR-[0-9]{3}' docs/DCTM_WOW_V1_Final_Architecture_Plan_v1.0.1.md | sort -u | wc -l)" -eq 202

if grep -HnE '^\[[A-Z][A-Z _-]+\]$|REMOVE IF UNUSED'   specs/001-dctm-v1-experience/plan.md   specs/001-dctm-v1-experience/research.md   specs/001-dctm-v1-experience/data-model.md   specs/001-dctm-v1-experience/work-packages.md   specs/001-dctm-v1-experience/assurance-plan.md
then
    echo "FAIL: unresolved template marker found"
    exit 1
else
    echo "PASS: no unresolved template markers"
fi
```

Expected: all structural tests succeed and the template-marker check prints `PASS: no unresolved template markers`.

Then review every register row: an unimplemented release verdict must remain `BLOCKED — evidence not yet produced`, never PASS.
