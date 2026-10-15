# Research plan (provisional)

## Question and motivation

Can a lightweight user-specific preference model learn which image-conditioned nostalgic edit a person prefers from only a few pairwise choices, while edits respect intended mood and preserve source content? Fixed preset selection is a useful baseline because it is simple and reproducible. Personalization must demonstrate held-out predictive value rather than merely fit feedback already seen.

## Hypotheses to test

1. A learned participant profile improves held-out pairwise preference prediction over fixed-rule and non-personalized baselines.
2. The benefit may increase with feedback count; evaluate budgets 0/2/5/10 choices, with uncertainty intervals and per-participant results.
3. Image conditioning and conservative strength settings may reduce content changes; measure this separately from preference.
4. Explanations assembled from recorded controls can be factually checked and may improve perceived control; this requires a user study.

These are hypotheses, not conclusions. Personalization of diffusion is already an active research area, so the novelty claim is currently unproven. The narrow contribution, if supported, would be low-feedback user preference ranking for source-conditioned nostalgic edits, with explicit preservation/intent evaluation.

## Architecture proposal

Mobile client -> FastAPI job API -> storage/job metadata -> configurable generation adapter. Phase 1 selects no production models. First executable research slice should be a synthetic-data-free, feature-vector pairwise ranking baseline: rule score, global Bradley–Terry logistic ranker, and participant-conditioned ranker. Then compare feedback budgets using participant-disjoint evaluation. Only after that is sound should real generation be considered.

Frozen CLIP image/text embeddings are a plausible candidate representation, not a decided dependency. They are not proof of mood or identity. A generation service must persist source and output separately and expose deletion. Explanations should report recorded controls and measured checks, not inferred model thoughts.

## Minimal first experiment proposal

Collect consented comparisons from participants viewing pairs of permitted, image-conditioned candidate edits from a small style set. Randomize left/right order and candidate seeds; capture mood, style, preferred candidate, optional reason, sequence/time and consent reference. Split by participant; for each held-out participant, provide only the prescribed number of their earlier interactions for personalization and score later comparisons. Compare fixed style rule, global pairwise ranker, and user-conditioned Bradley–Terry ranker. Report pairwise accuracy, log loss, confidence intervals, and per-user distribution. A pilot is for protocol/debugging, not a powered efficacy claim. Do not recruit or collect yet.

## Threats and controls

- Candidate-generation randomness and style confounding: use matched source, prompt, settings, and seeds where feasible; record all generation metadata.
- Leakage: source/participant grouping and split decisions must be declared before analysis.
- Sparse user data: report cold-start and individual variability; avoid overstating average improvements.
- Emotion labels are observer/category judgments, not ground truth about a person’s internal state.
- Identity metrics can fail across demographics and do not replace human review.
- Human-subject research requires institutional ethics determination before collection.
