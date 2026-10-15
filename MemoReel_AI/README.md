# MemoReel AI

Research prototype for personalized nostalgic image editing. Current status: Phase 1 foundation only. No models or generated media were added.

## Phase 0 findings

- Existing local folders were found on a second listing: `text_emotion_dataset/` contains GoEmotions files, code, plots and a model card; `image_emotion_dataset/test/` contains images in `angry`, `disgust`, and `fear` folders. Provenance, rights and intended use remain unconfirmed; they were preserved and not used in experiments.
- Windows PowerShell 5.1 and Python 3.11.9 via `py -3.11` are available. `python` itself resolves to a Microsoft Store alias. Installed packages are pip 24.0 and setuptools 65.5.0 only; no ML libraries are installed.
- RAM/GPU queries were denied or unavailable, and C: free space was not reported. Hardware and usable storage remain unverified.
- No dataset or model downloads were made in this work.

## Research direction

The project studies whether a small number of per-person pairwise choices can improve ranking of nostalgic edits, subject to content-preservation and user-intent constraints. This is a hypothesis, not a result or established novelty claim. See `docs/` for the provisional plan and literature review.

## Setup

Requires Python 3.11+ (uses standard-library `tomllib`) to run the initial schema/config tests:

```powershell
py -3.11 -m unittest discover -s tests -v
```

No third-party Python dependency is needed for Phase 1. Install Python only through your normal approved environment; do not download model weights or datasets for this phase.

## Data and privacy

Do not place originals in generated-output folders. Do not add private photographs or preference feedback to research data without informed, explicit consent and an approved protocol. Existing dataset folders need provenance and rights review before use; see `LICENSE_REVIEW.md` and `docs/dataset_card.md`.
