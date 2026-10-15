# Initial experiment protocol (proposal)

## Primary outcome

Held-out within-participant pairwise prediction accuracy, supplemented by log loss and participant-level confidence intervals. Split at participant level for user-independent generalization. Personalization adaptation for held-out users uses only their early feedback at fixed budgets; later choices are test-only. Also report cold-start global baseline.

## Comparators

1. Fixed rule-based style mapping (pre-registered mapping from requested mood to style).
2. Generic ranker trained on other participants, no user feature.
3. Same ranker plus an explicitly user-specific profile adapted from the permitted feedback budget.

## Data and controls

Use paired candidates from the same source and requested intent, record model/version, prompt, seed, strength, adapter and timestamp. Randomize display side. Group by source and participant in split checks. Deduplicate candidate IDs and avoid source overlap where needed to prevent memorization. Decide whether source-disjoint generalization is required based on study design.

## Analysis

Predefine exclusions and tie handling; report sample counts, missingness, uncertainty, calibration, per-user variability and qualitative failure modes. No causal claims from observational feedback. Report preference, preservation, mood-alignment judgments, explanation factuality and latency as distinct endpoints. Metrics such as SSIM/LPIPS are supporting measures, not substitutes for human review or identity evaluation.

## Reproducibility

Version config, source commit, split manifest, seeds, model identifiers/revisions, environment, raw annotation provenance and analysis code. Store actual row-level predictions and aggregate tables generated from those rows. No experiment has been run.
