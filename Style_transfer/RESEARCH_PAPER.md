# Emotion-Aware Multimodal Nostalgic Photo Styling: A Rule-Based Web System for Caption–Image Contextualization

**Manuscript status:** Implementation-based system paper. This draft reports repository-verifiable behavior. No classifier benchmark or user study is claimed because neither trained checkpoints nor measured evaluation results are included in the repository.

**Authors:** [Oviya Ragothamana, Sushma pokala, Sammangi Gopi Chand, Raghu paladi]  
**Affiliation:** [SCOPE, VIT, Vellore, Country]  
**Corresponding author:** [Email]

## Abstract

This paper presents MemoriaAI, a web application that transforms a user-provided photograph and caption into a themed visual memory artifact. The system combines image statistics, a keyword-based caption affect analyzer, rule-based modality fusion, a lexical nostalgia score, deterministic style selection, pixel-level photographic grading, narrative templates, and an explanation dashboard. A React single-page interface communicates with a FastAPI service; a browser-side fallback can perform a parallel simplified workflow when the service is unavailable. Six presets implement channel-wise color transformations, contrast and saturation adjustment, optional blur blending, Gaussian film grain, and radial vignetting. Captions are tokenized and matched against emotion and temporal-memory lexicons. A weighted rule table maps predicted image/text labels and caption cues to a named memory category; a bounded score aggregates temporal markers, reminiscence terms, affective compatibility, and supplied confidence values. The system also returns template-generated prose and token-level lexicon weights, plus a synthetic Gaussian heatmap overlay.

The repository includes FER-style image folders and GoEmotions files, but no runtime training pipeline, learned checkpoint, or dataset-linked evaluation output. Image emotion is inferred from global RGB statistics, while text emotion uses fixed keyword weights rather than a transformer. Explanation outputs are heuristic and synthetic rather than SHAP or gradient-derived Grad-CAM. Thus accuracy, precision, recall, F1, confusion matrices, user outcomes, and comparative performance cannot be reported as measured findings. The contribution is an inspectable prototype for affect-conditioned photo styling and memory presentation, with an explicit validation gap. Claims of predictive validity require controlled evaluation against labeled and human-rated data.

## Keywords

Multimodal affect, nostalgic image styling, emotion analysis, rule-based fusion, image processing, explainable interfaces, GoEmotions, FER-2013.

## 1. Introduction

### A. Background

Personal photographs are often shared with captions that supply context unavailable from pixels alone. A reunion photograph, for example, can express happiness while its caption emphasizes elapsed time or longing. Research characterizes nostalgia as a self-relevant, socially grounded, and often ambivalent emotion rather than a simple positive/negative polarity [1]–[3]. This motivates systems that treat caption and image cues together and let the resulting interpretation influence a creative transformation.

MemoriaAI is a prototype for this interaction. It accepts one image and one caption, assigns coarse affect labels using lightweight heuristics, combines them with explicit caption rules, chooses an analog-photo preset, and produces a styled image with narrative and explanatory interface elements. It is implemented as a web product rather than as a learned image-to-image generative model.

### B. Problem Statement

Generic photo filters apply an aesthetic without considering the personal meaning stated in a caption. The repository addresses the product-design problem of making photo styling responsive to both a photograph’s global appearance and its accompanying memory text. The operational objective is to turn these inputs into a reproducible bundle: affect labels, a fused memory category, a bounded nostalgia index, a selected style, a processed image, narrative text, and an explanation view.

This objective should not be confused with a validated psychological measurement task. The code defines a heuristic “nostalgia score,” but no annotated nostalgia dataset, calibration procedure, or human-rating study establishes that the value measures perceived nostalgia.

### C. Motivation and Objectives

The project’s motivation is to make memory-oriented photo creation accessible through a browser interface and to expose some of the rules used to select styles. The implementation objectives are:

1. accept an image and caption through a web application and API;
2. infer simple image and text affect categories;
3. fuse the categories with explicit contextual overrides;
4. compute a bounded score from temporal and reminiscence cues;
5. apply one of six selectable photographic transformations;
6. return a narrative, explanation fields, and persistent history where storage succeeds.

### D. Contributions

The repository supports the following implementation contributions: (i) an end-to-end browser/server workflow joining image styling with caption context; (ii) an interpretable, rule-based pipeline with accessible intermediate outputs; (iii) six configurable analog-film-inspired color transformations; (iv) an API and optional memory-history schema; and (v) a browser-side fallback. These are engineering contributions, not novel learned algorithms. The system also surfaces a valuable research gap: the included corpora and analysis scripts are not integrated with the live application models.

## 2. Literature Review

### A. Emotion and Nostalgic Memory

Psychological work describes nostalgia as a meaningful autobiographical experience that commonly includes social relationships, positive affect, and a sense of temporal distance, while retaining bittersweet elements [1]–[3]. These findings motivate the prototype’s use of reunion, family, childhood, and elapsed-time markers. They do not validate its chosen lexicons or scoring weights. In particular, the implementation treats keyword presence as evidence and does not model autobiographical memory, event context, or individual differences.

### B. Text Emotion Resources

GoEmotions provides 58,009 English Reddit comments annotated with 27 emotion categories and Neutral [4]. The repository contains the original train, development, and test TSV files (43,410, 5,426, and 5,427 examples as described by the bundled dataset documentation), raw annotation CSV files, mappings, and analysis scripts. GoEmotions is a multi-label dataset with a particular source population and annotation process. Its presence alone does not imply that MemoriaAI trains on it. The runtime text service instead uses a hand-authored mapping of words to six output categories and nostalgia cues. Fine-grained emotion classification with pretrained transformers is an established alternative, but no such model is loaded by the application.

### C. Facial Affect and Image Datasets

FER-2013 is a widely used facial-expression benchmark introduced in the representation-learning challenges [5]. The project’s image directory has a `train` and `test` layout and seven class names, but the current checked-in directory contains only four training classes (`angry`, `disgust`, `fear`, `happy`) and all seven test classes; the apparent train/test setup is incomplete for a conventional seven-class experiment. More fundamentally, runtime image analysis does not use this dataset or a trained face model. It computes global color means, channel standard deviations, brightness, and a warmth ratio. Global color is a scene property and cannot establish that a face exists or that a subject is smiling.

### D. Multimodal Learning and Explainability

Multimodal systems commonly combine representations or predictions from multiple modalities; late fusion is a practical design when modality-specific components are separate [6]. MemoriaAI’s fusion is a hand-coded label-pair lookup with caption overrides and a confidence-weighted scalar, rather than learned cross-attention. SHAP defines feature attribution through Shapley values [7], while Grad-CAM derives spatial importance from gradients with respect to convolutional feature maps [8]. The project uses neither algorithm: token weights are constants from a lexicon, and its heatmap is a fixed pair of Gaussian peaks blended with the input. These outputs can be useful as illustrative interface cues, but they are not faithful attributions of a predictive model.

### E. Positioning and Research Gap

The nearest methodological references are affect datasets, multimodal fusion, image-processing operations, and explainability methods. MemoriaAI’s distinguishing aspect is the product integration of caption-conditioned style selection, nostalgic presentation, and a memory archive. The research gap is not a demonstrated accuracy advantage over prior classifiers; it is the lack of a validated, user-centered pipeline that connects multimodal affect interpretation to creative photo styling. The present repository is an initial deterministic system toward that product goal. Comparative model performance remains untested.

## 3. Proposed Methodology

### A. Data Collection and Available Corpora

At inference time, the user supplies an image and free-form caption. No user data collection protocol, consent workflow, or annotation campaign is implemented. The repository includes two external corpora for potential research use:

| Resource | Repository contents | Intended relevance | Use in current runtime |
|---|---|---|---|
| GoEmotions | `train.tsv`, `dev.tsv`, `test.tsv`; three raw CSV files; emotion/mapping resources; analysis scripts | Fine-grained text emotion research | None; no application training or inference adapter |
| FER-style image folders | `train` and `test`, emotion-named directories | Facial-expression research | None; training folders are incomplete (four of seven classes) |

The image folder counts shown in the repository are not treated as an evaluation set because the runtime has no trained model and no evaluation script linking its predictions to these files. No dataset license/provenance audit is added by the application.

### B. Preprocessing and Feature Engineering

The backend decodes base64 image data using Pillow and converts it to RGB. Image analysis computes channel means \(\mu_R,\mu_G,\mu_B\), channel standard deviations, mean brightness \(B=(\mu_R+\mu_G+\mu_B)/3\), relative warmth \(W=(\mu_R-\mu_B)/\max(B,1)\), and mean channel deviation \(C=(\sigma_R+\sigma_G+\sigma_B)/3\). Hand-coded thresholds update fixed scores for Happy, Sad, Angry, Neutral, and Surprise, after which scores are normalized to sum to one. The `deepface` package is probed at initialization but never called by the analysis routine. A fallback returns a default Happy label on decoding or analysis exceptions.

Caption preprocessing lowercases and extracts alphabetic tokens with apostrophes. The service initializes six affect scores and increments them by fixed amounts for exact token matches in five emotion lexicons. A sixth lexicon tracks temporal or nostalgic words. Additional substring rules boost scores for patterns such as “finally” with “together,” “miss” with “school” or “days,” and “best years.” The normalized maximum is returned as the text emotion. This is a normalized weighted rule score, not a calibrated posterior probability.

### C. Fusion and Nostalgia Index

Let \(e_v\) and \(e_t\) be the maximum-scoring image and text labels, and \(c_v,c_t\) their normalized scores. Fusion applies a lookup table \(\Phi(e_v,e_t)\), then may overwrite the category based on caption substrings indicating friends/reunion, family, or childhood. Its synergy value is

\[
\Psi=0.45c_v+0.55c_t.
\]

The score is built from temporal evidence \(T\), lexical reminiscence density \(D\), emotion-pair resonance \(R\), and confidence contribution \(Q\):

\[
S=\operatorname{round}\left[\min(98,\max(45,T+D+R+Q)\right], \quad
Q=15\frac{c_v+c_t}{2}.
\]

The implementation caps \(T\) at 35 and \(D\) at 30; it assigns resonance using a small set of affect-pair rules and caps it at 20. The final score is bounded 45–98 except for a hard-coded benchmark condition (“5 years” and “together again”) that assigns 91. This exception makes the score deterministic for the example but weakens its interpretation as a general scoring function. The README’s documented range of 0–100 is broader than the actual score floor/cap.

### D. Style Selection and Image Transformation

Six presets (Kodak 90s, Golden Warm, Polaroid Effect, Analog Camera, Sepia Dreamscape, and 70s Kodachrome) contain target categories, default warmth/grain/vignette/fade parameters, palettes, and descriptive diffusion prompts. The prompt is returned as metadata; no diffusion model is invoked. Style is chosen first through exact target-category matching and then through category keyword matching, with Kodak 90s as the default. A caller may override the style using a valid preset slug.

For an RGB image \(I\), the selected preset modifies channels through fixed multipliers and offsets. For example, Kodak styling raises red and green, attenuates blue, and lifts the channel values according to fade. The pipeline then changes contrast and saturation, optionally blends a Gaussian-blurred image for golden/sepia presets, adds per-pixel Gaussian noise with a shared spatial noise plane, and multiplies by a radial vignette mask. Images exceeding 1600 pixels on a side are resized proportionally. Output is JPEG quality 92 and base64 encoded. This is deterministic in structure but stochastic in grain because no random seed is set.

### E. Narrative and Explanation Generation

The story service selects from category-specific fixed prose templates; the selected template may vary randomly. The explanation service assigns static lexicon weights, emits default keywords when no listed cue is found, and selects a fixed 57/43 or 48/52 caption/image split according to a threshold on summed text weights. The visual heatmap uses two Gaussian peaks at fixed relative image coordinates, applies a synthetic color map and blur, and blends the result with the original. Neither image faces nor model gradients are computed. The explanation is therefore a trace of designed rules rather than a faithful explanation of a learned model.

### F. Algorithm

**Algorithm 1: Runtime memory processing**

1. Receive caption \(T\), image bytes \(I\), and optional style override.
2. Decode \(I\); compute global pixel statistics; threshold into \(e_v,c_v\).
3. Tokenize \(T\); apply emotion lexicons and contextual rules to obtain \(e_t,c_t\).
4. Lookup \(\Phi(e_v,e_t)\); apply caption-category overrides; compute \(\Psi\).
5. Compute \(T,D,R,Q\); return bounded nostalgia score \(S\), including the specific 91-point override.
6. Select a preset or apply the validated override; perform color grading, grain, and vignette.
7. Select a story template and construct lexicon-based explanation fields and synthetic heatmap.
8. Return all component results; attempt to persist a memory record.

## 4. System Design

### A. Architecture Overview

The production-style path is a React 18/Vite frontend sending JSON requests to FastAPI. The backend routes orchestrate Python services and Pydantic schemas; SQLAlchemy maps memory history to SQLite by default or a configured SQLAlchemy database URL. When the local backend is unavailable, the frontend executes its own heuristic pipeline and stores up to 30 records in browser `localStorage`.

**Fig. 1.** *MemoriaAI processing architecture.* User image and caption flow from the React/Vite interface to FastAPI. Image statistics and caption lexicons produce separate labels; rule fusion and scoring feed preset selection, Pillow/NumPy filters, template narrative generation, and heuristic explanation. The response is displayed in the dashboard and may be archived through SQLAlchemy or browser storage. Draw this as two parallel modality branches converging on a rule-based fusion node, followed by four output branches (score, style, story, explanation).

### B. Modules and APIs

| Module | Responsibility | Main implementation |
|---|---|---|
| Frontend | Upload, results, styling controls, history, export-oriented UI | React 18, Vite, Tailwind CSS, browser Canvas, localStorage fallback |
| Image emotion | RGB-statistic heuristic and confidence-like normalized scores | Pillow `ImageStat`; optional DeepFace import check only |
| Text emotion | Token matching and context boosts | Python regular expressions and fixed word lists |
| Fusion | Label-pair lookup, caption overrides, weighted score | Python dictionaries and string matching |
| Nostalgia score | Temporal and semantic cue accumulation plus affect rules | Regex, lexicons, fixed caps, benchmark override |
| Style transfer | Six photographic looks and image encoding | Pillow, NumPy, Gaussian noise, radial mask |
| Story generation | Category-conditioned text output | Fixed templates; random template choice |
| Explanation | Token weights, modality split, Gaussian heatmap | Fixed lexicon and image-coordinate formulas |
| Persistence | Memory history and delete operations | SQLAlchemy `memories` table; SQLite default |
| REST API | Component and combined pipeline endpoints | FastAPI, Pydantic request/response models |

The principal endpoints are `POST /emotion/image`, `POST /emotion/text`, `POST /fusion`, `POST /nostalgia-score`, `POST /generate-style`, `POST /generate-story`, `POST /explanation`, and `POST /process-memory`, with `GET /history`, `DELETE /history/{id}`, `GET /styles`, and `GET /health`. OpenAPI documentation is served at `/docs`.

### C. Data Model and Technical Design

The SQLAlchemy `MemoryRecord` table stores a UUID, caption, image references, emotion labels/confidences, fused category, score, style, story, explanation contributions, serialized keywords/reasons, and creation timestamp. The current processing route saves truncated base64 strings (first 200 characters plus a marker) into URL-named fields, so database history does not preserve a complete retrievable image. Database errors are caught and treated as nonfatal. The UI falls back to browser storage when the backend is offline. CORS is configured permissively (`*`), and the supplied Dockerfile packages a Python 3.10 slim service.

## 5. Experimental Setup and Reproducibility

### A. Software Environment

The backend requirements specify Python 3.10+ and FastAPI, Uvicorn, Pydantic/Pydantic Settings, SQLAlchemy, Pillow, NumPy, SciPy, requests, pytest, and HTTPX. DeepFace, PyTorch, torchvision, and Transformers are commented optional dependencies. The frontend uses React 18, Vite 5, Tailwind CSS 3, and Lucide React. There is no lockfile in the listed repository. No fixed runtime, OS build, GPU, processor, memory, or device configuration is recorded; therefore hardware cannot be reported reproducibly.

### B. Training Parameters

No application model training script, optimizer, batch size, epoch count, seed, model checkpoint, or trained-model inference call is present. GoEmotions includes upstream data analysis and metric utilities, but no BERT classifier source is included in this repository snapshot. The app config names model identifiers and sets `USE_DEEP_LEARNING_MODELS=False`; these settings are not used to load models in the services. Consequently, there are no training parameters to report.

### C. Evaluation Protocol and Metrics

The repository contains seven API tests covering health, styles, text response shape, fusion response shape, a hard-coded nostalgia example, story output, and explanation output. These are software contract checks rather than a labeled predictive-performance evaluation. The GoEmotions `calculate_metrics.py` script can calculate multilabel accuracy, precision, recall, and F1 from an external predictions file at threshold 0.3, but no predictions or generated metrics JSON are included. No confusion matrix, ablation, comparative experiment, latency benchmark, or human evaluation is present. The tests were not run as part of this manuscript preparation.

## 6. Results and Analysis

### A. Implemented Outputs

The implementation supports an end-to-end response with image/text labels, category, score factors, selected style, processed JPEG, story text, explanation fields, and timestamp. The only exact numerical example documented in the backend test is a score of 91 for captions containing both “5 years” and “together again”; this is a deliberate branch in source code and is not a measured model result. The API test file asserts successful response shapes and expected service behavior, but provides no held-out sample predictions or ground-truth labels.

### B. Classification Metrics

| Metric | Image emotion | Caption emotion | Nostalgia score |
|---|---:|---:|---:|
| Accuracy | Not measured | Not measured | Not applicable / not measured |
| Precision | Not measured | Not measured | Not measured |
| Recall | Not measured | Not measured | Not measured |
| F1 score | Not measured | Not measured | Not measured |
| Confusion matrix | Not available | Not available | Not applicable |

Reporting numeric accuracy or F1 would be unsupported: labels produced by rules are not compared with ground truth. The score is a heuristic index, not a classifier whose correctness is measured in the repository.

### C. Comparative Results

No comparison against DeepFace, DistilRoBERTa, CLIP, neural style transfer, or a baseline is executed. These names appear in documentation or settings, but the application does not instantiate those models. A fair comparison would require a held-out dataset, explicit target labels, fixed preprocessing, seeded inference, and human ratings for aesthetic and narrative outcomes. Until that experiment is run, no improvement claim can be made.

### D. Qualitative Technical Analysis

The most defensible observed result is functional composition: the repository defines a path from user inputs to a styled image and structured metadata. The image transformation is a conventional filter pipeline and should preserve broad scene geometry, unlike generative image-to-image models. Rule traces are inspectable, but behavior can be brittle: exact strings and substring matching fail under paraphrase, negation, polysemy, and multilingual text. Global color statistics can confound illumination, camera white balance, and scene content with emotion. The system also contains stochastic outputs through grain and story template selection, while its browser fallback and backend do not share identical inference rules.

## 7. Discussion

### A. Interpretation

The project demonstrates an application architecture for affect-conditioned creative editing, not empirical evidence that the system recognizes emotion accurately or produces more nostalgic results than alternatives. Its “multimodal” quality lies in the orchestration of image- and text-derived heuristics, not in learned multimodal representations. Its score can be interpreted only as an implementation-defined cue aggregate. It has no psychometric scale development, calibration, or criterion validity.

### B. Strengths

The pipeline is modular and comparatively easy to inspect. Its API separates stages, the frontend provides a unified workflow, six presets expose tangible creative variation, and the rules yield understandable intermediate values. The conventional filter path is lightweight and avoids requiring model downloads. The browser fallback can preserve a demo experience without a backend. Bundled public datasets provide a possible starting point for future model training, subject to dataset provenance and bias review.

### C. Limitations and Validity Threats

First, global RGB statistics do not detect faces, and response fields such as “face detected” and facial-expression cues are assigned heuristically. Second, the text service is a small English lexicon with exact-token matching; scores are mislabeled as confidence if interpreted probabilistically. Third, the scoring rules and hard-coded 91-point exception are unvalidated. Fourth, reported “SHAP” token importance is fixed lexical weighting and “Grad-CAM” is a coordinate-based Gaussian overlay; neither is model attribution. Fifth, story templates are generic category-specific strings, not caption-grounded generation except for one special case. Sixth, image dataset training is incomplete in the current checkout, and there is no training integration or model checkpoint. Seventh, GoEmotions is Reddit English data and the README itself notes demographic and source biases; it may not transfer to personal captions. Finally, evaluation on API contracts alone cannot support claims about user satisfaction, fairness, privacy, or predictive quality.

## 8. Conclusion

This paper described MemoriaAI, an implementation of an emotion-aware nostalgic photo-styling web application. Its central workflow combines pixel-statistic image heuristics, keyword-driven caption labels, rule-based fusion and nostalgia scoring, six photographic filter presets, templated narrative output, heuristic explanation artifacts, and optional memory persistence. The implementation is concrete and modular, but the checked-in system does not include trained application models or empirical evaluation outputs. It therefore supports claims about architecture and implemented transformations, not accuracy, superiority, calibrated nostalgia measurement, or faithful explainability. The repository provides a foundation for a subsequent validated system after replacing heuristic classifiers, connecting data to a documented training pipeline, and running controlled evaluations.

## 9. Future Scope

1. Integrate a documented facial-emotion model and a trained multi-label text classifier, with versioned checkpoints, licensing, and inference tests.
2. Complete and audit the image splits; establish subject-independent train/validation/test partitions and report class-wise metrics and confusion matrices.
3. Evaluate GoEmotions models with threshold selection on validation data, macro/micro/weighted metrics, calibration, and domain-specific captions annotated by multiple raters.
4. Develop and validate a human-rated nostalgia instrument; test score reliability, construct validity, and sensitivity to image/text disagreement.
5. Replace synthetic explanations with perturbation-tested SHAP values and gradient-based heatmaps tied to the actual prediction model; report faithfulness limitations.
6. Conduct ablation and baseline studies comparing image-only, text-only, rule-fusion, and learned-fusion systems.
7. Run a user study measuring perceived aesthetic quality, emotional fit, trust, and narrative usefulness; preregister hypotheses and report participant demographics.
8. Improve reproducibility with dependency lockfiles, deterministic seeds, device/version records, evaluation scripts, saved outputs, and model cards.
9. Improve privacy and reliability through complete asset storage, retention controls, upload validation, restricted CORS, and transparent consent for personal photographs.

## 10. References

[1] C. Sedikides, T. Wildschut, J. Arndt, and C. Routledge, “Nostalgia: Past, present, and future,” *Current Directions in Psychological Science*, vol. 17, no. 5, pp. 304–307, 2008, doi: 10.1111/j.1467-8721.2008.00595.x.

[2] C. Sedikides and T. Wildschut, “Finding meaning in nostalgia,” *Review of General Psychology*, vol. 22, no. 1, pp. 48–61, 2018, doi: 10.1037/gpr0000109.

[3] T. Wildschut, C. Sedikides, J. Arndt, and C. Routledge, “Nostalgia: Content, triggers, functions,” *Journal of Personality and Social Psychology*, vol. 91, no. 5, pp. 975–993, 2006, doi: 10.1037/0022-3514.91.5.975.

[4] D. Demszky, D. Movshovitz-Attias, J. Ko, A. Cowen, G. Nemade, and S. Ravi, “GoEmotions: A dataset of fine-grained emotions,” in *Proc. 58th Annu. Meeting Assoc. Comput. Linguistics*, 2020, pp. 4040–4054, doi: 10.18653/v1/2020.acl-main.372.

[5] I. J. Goodfellow *et al*., “Challenges in representation learning: A report on three machine learning contests,” in *Neural Information Processing*, vol. 2, 2013, pp. 117–124, arXiv:1307.0414.

[6] T. Baltrušaitis, C. Ahuja, and L.-P. Morency, “Multimodal machine learning: A survey and taxonomy,” *IEEE Trans. Pattern Anal. Mach. Intell.*, vol. 41, no. 2, pp. 423–443, 2019, doi: 10.1109/TPAMI.2018.2798607.

[7] S. M. Lundberg and S.-I. Lee, “A unified approach to interpreting model predictions,” in *Advances in Neural Information Processing Systems*, vol. 30, 2017.

[8] R. R. Selvaraju *et al*., “Grad-CAM: Visual explanations from deep networks via gradient-based localization,” in *Proc. IEEE Int. Conf. Comput. Vis. (ICCV)*, 2017, pp. 618–626, doi: 10.1109/ICCV.2017.74.

[9] L. A. Gatys, A. S. Ecker, and M. Bethge, “A neural algorithm of artistic style,” *Journal of Vision*, vol. 16, no. 12, Art. no. 326, 2016, doi: 10.1167/16.12.326.

[10] A. Krizhevsky, I. Sutskever, and G. E. Hinton, “ImageNet classification with deep convolutional neural networks,” in *Advances in Neural Information Processing Systems*, vol. 25, 2012, pp. 1097–1105.

[11] A. Vaswani *et al*., “Attention is all you need,” in *Advances in Neural Information Processing Systems*, vol. 30, 2017.

[12] V. Sanh, L. Debut, J. Chaumond, and T. Wolf, “DistilBERT, a distilled version of BERT: Smaller, faster, cheaper and lighter,” in *Proc. 5th Workshop Energy Efficient Machine Learning and Cognitive Computing*, 2019, arXiv:1910.01108.

[13] J. Devlin, M.-W. Chang, K. Lee, and K. Toutanova, “BERT: Pre-training of deep bidirectional transformers for language understanding,” in *Proc. NAACL-HLT*, 2019, pp. 4171–4186, doi: 10.18653/v1/N19-1423.

[14] S. Mohammad and P. Turney, “Crowdsourcing a word-emotion association lexicon,” *Computational Intelligence*, vol. 29, no. 3, pp. 436–465, 2013, doi: 10.1111/j.1467-8640.2012.00460.x.

[15] C. O. S. Sorensen, “A review of the literature on emotion recognition from text,” in *Proc. 2017 IEEE Int. Conf. Data Mining Workshops*, 2017, pp. 985–991.

[16] P. Ekman, “An argument for basic emotions,” *Cognition and Emotion*, vol. 6, no. 3–4, pp. 169–200, 1992, doi: 10.1080/02699939208411068.

[17] J. A. Russell, “A circumplex model of affect,” *Journal of Personality and Social Psychology*, vol. 39, no. 6, pp. 1161–1178, 1980, doi: 10.1037/h0077714.

[18] J. Deng *et al*., “ImageNet: A large-scale hierarchical image database,” in *Proc. IEEE Conf. Comput. Vis. Pattern Recognit.*, 2009, pp. 248–255, doi: 10.1109/CVPR.2009.5206848.

[19] A. Krizhevsky and G. Hinton, “Learning multiple layers of features from tiny images,” Univ. Toronto, Toronto, ON, Canada, Tech. Rep., 2009.

[20] K. Simonyan and A. Zisserman, “Very deep convolutional networks for large-scale image recognition,” in *Proc. Int. Conf. Learning Representations*, 2015, arXiv:1409.1556.

[21] S. J. Pan and Q. Yang, “A survey on transfer learning,” *IEEE Trans. Knowl. Data Eng.*, vol. 22, no. 10, pp. 1345–1359, 2010, doi: 10.1109/TKDE.2009.191.

[22] A. Mehrabian and J. A. Russell, *An Approach to Environmental Psychology*. Cambridge, MA, USA: MIT Press, 1974.

## 11. Appendix

### A. Screenshot and Output Placeholders

No saved application screenshots or evaluation graphs are present in the inspected repository. The following figures should be captured from a verified run before submission; do not represent these placeholders as experimental evidence.

- **Fig. 2. Landing and upload interface.** Capture the image upload control, caption field, preset selector, and processing entry point.
- **Fig. 3. Results dashboard.** Capture original/styled comparison, selected preset, score gauge, and emotion/category cards for a documented input.
- **Fig. 4. Explanation panel.** Capture the current lexical cue list and Gaussian overlay; caption it “heuristic cue and synthetic heatmap visualization,” not SHAP/Grad-CAM attribution.
- **Fig. 5. Memory history.** Capture the browser or backend history view and disclose which storage mode produced it.
- **Fig. 6. API response example.** Include a redacted `/process-memory` JSON response, image removed, with implementation version and input caption.

### B. Architecture Diagram Description

Use Fig. 1’s architecture description in Section IV. Show the backend and browser fallback as separate paths because their rules and persistence differ. Label all inference components “heuristic” and the explanation heatmap “synthetic Gaussian overlay.”

### C. Reproducibility Checklist

For an empirical extension, archive: repository commit hash; OS/CPU/GPU and memory; Python and Node versions; resolved dependency files; input dataset version and licenses; class counts per split; model identifiers and checkpoint hashes; random seeds; evaluation scripts; raw predictions; metric outputs; confusion matrices; and screenshots with test inputs. The current repository does not include this complete record.

---

# Separate Project Abstract

MemoriaAI is a web-based prototype for turning a photograph and its caption into a nostalgic visual keepsake. The application analyzes image-wide color statistics and caption keywords, combines the resulting labels with rule-based fusion, computes a bounded nostalgia cue score, selects one of six analog-inspired photographic styles, and returns a filtered image with a category-specific story and explanation view. A React/Vite frontend communicates with a FastAPI backend, with browser-side processing and local history available when the backend is offline. The backend uses Pillow and NumPy for color grading, blur blending, grain, and vignette effects; SQLAlchemy provides optional memory-history persistence. Although the repository includes FER-style image folders and the GoEmotions corpus, these datasets are not connected to runtime training or inference, and no trained checkpoints or benchmark predictions are included. Image and text emotion outputs are therefore heuristic, and the dashboard’s keyword weights and Gaussian heatmap are not SHAP or Grad-CAM explanations. The implementation demonstrates an end-to-end creative workflow, while quantitative accuracy and human-centered claims remain to be evaluated.

# Journal Paper Title Suggestions

1. **Emotion-Aware Multimodal Nostalgic Photo Styling: A Rule-Based Web System for Caption–Image Contextualization**
2. **From Caption and Color to Keepsake: An End-to-End Prototype for Nostalgia-Oriented Photo Styling**
3. **A Modular Web Pipeline for Caption-Conditioned Analog Photo Effects and Memory Presentation**
4. **Design and Implementation of a Heuristic Multimodal System for Nostalgic Image Transformation**
5. **Integrating Text Cues, Image Statistics, and Photographic Filters for Digital Memory Artifacts**

# One-Page Conference Presentation Summary

## MemoriaAI: A Rule-Based Multimodal Photo Keepsake System

**Problem.** Standard photo filters are selected independently of the story attached to an image. A caption can add temporal and social context that changes how a user wants a photograph to look.

**System.** MemoriaAI is a web application that accepts an image and caption, estimates coarse affect using image statistics and keyword rules, maps the pair to a memory category, computes an implementation-defined nostalgia score, selects an analog-inspired filter, and returns a styled image, narrative card, and explanation panel. Its stack is React 18/Vite, FastAPI, Pillow/NumPy, Pydantic, SQLAlchemy, and SQLite by default. Six presets implement channel grading, contrast/saturation changes, optional blur blending, film grain, and radial vignette. The backend exposes individual stage APIs and an end-to-end `/process-memory` endpoint; a browser fallback provides a simplified offline workflow.

**Pipeline.** (1) RGB means, channel deviations, brightness, and relative warmth yield a heuristic image label. (2) A token lexicon and context rules yield one of six text labels and memory cues. (3) A lookup table and caption overrides produce a fused category. (4) Temporal cues, reminiscence terms, affect rules, and confidence-like scores form a bounded 45–98 index, with a fixed benchmark case set to 91. (5) Category-to-preset rules select a style; Pillow/NumPy render the result. (6) A template story and heuristic explanation fields are returned and optionally archived.

**What the repository establishes.** The application architecture and transformations are implemented. The repository contains GoEmotions files and FER-style folders, plus API contract tests. It does not contain application model training, trained model checkpoints, measured predictions, metric outputs, confusion matrices, or user-study results. The configured DeepFace/Transformer names do not correspond to runtime model calls. The explanation panel’s token weights are fixed lexicon values, and its visual overlay is Gaussian-generated rather than gradient-based attribution.

**Contribution.** The project contributes a modular and inspectable product prototype for linking caption context to nostalgic photo styling, including a complete API/UI workflow and offline fallback. It should be presented as a system-design and implementation paper, not as a validated emotion-recognition or explainable-AI result.

**Next experiment.** Train or integrate versioned affect models; complete the image dataset split; annotate a domain-specific caption/image set; compare image-only, text-only, and fused systems using macro/micro precision, recall, F1, accuracy, and confusion matrices; measure score validity and style-emotion fit with independent human ratings; and report reproducible device/software settings and model attribution faithfulness.

# Novel Contributions List (Implementation-Level)

1. End-to-end integration of caption cues, image statistics, style selection, output rendering, story presentation, and memory history in one web workflow.
2. Explicit rule-based cross-modal category mapping and caption-context overrides that can be inspected and reproduced.
3. Six configurable analog-film-inspired image transformations implemented with standard pixel operations rather than requiring a generative model.
4. A multi-factor nostalgia cue score that exposes temporal, semantic, affective, and confidence components, while remaining an unvalidated heuristic.
5. A browser-side fallback path that preserves a simplified editing and local-history experience when the API is unavailable.
6. A clear engineering baseline for future studies that can compare rules with trained models and can replace synthetic explanations with tested attribution methods.

These contributions describe the repository’s implemented design. They should not be presented as algorithmic novelty or empirical superiority without comparison and validation.
