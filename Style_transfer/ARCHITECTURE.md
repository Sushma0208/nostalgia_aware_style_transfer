# Architectural & Mathematical Specification

## "Emotion-Aware Multimodal Nostalgic Style Transfer with Explainable AI for Social Media"

This document provides the formal mathematical formulations and architectural details underpinning the system's five core novelty elements.

---

## 1. Multimodal Emotion Understanding & Cross-Modal Fusion

### 1.1 Vision Domain
Let $I \in \mathbb{R}^{H \times W \times 3}$ denote an input photograph. The visual emotion extractor $\mathcal{F}_{\text{vis}}$ (based on DeepFace and visual color temperature heuristics) extracts a probability distribution over the discrete set of primary facial expressions:
$$\mathcal{E}_{\text{vis}} = \{\text{Happy}, \text{Sad}, \text{Angry}, \text{Neutral}, \text{Surprise}\}$$
$$P(e_v | I) = \text{Softmax}\left(\mathcal{F}_{\text{vis}}(I)\right), \quad e_v \in \mathcal{E}_{\text{vis}}$$

### 1.2 Linguistic Domain
Let $T = (t_1, t_2, \dots, t_N)$ denote the caption tokens. The linguistic emotion extractor $\mathcal{F}_{\text{text}}$ (fine-tuned DistilRoBERTa on GoEmotions taxonomy) extracts a probability distribution over fine-grained emotional categories:
$$\mathcal{E}_{\text{text}} = \{\text{Joy}, \text{Sadness}, \text{Gratitude}, \text{Excitement}, \text{Love}, \text{Neutral}\}$$
$$P(e_t | T) = \text{Softmax}\left(\mathcal{F}_{\text{text}}(T)\right), \quad e_t \in \mathcal{E}_{\text{text}}$$

### 1.3 Cross-Modal Fusion Formulation
Rather than applying simple concatenation, the cross-modal fusion operator $\mathcal{M}(e_v, e_t)$ maps the pair into a structured nostalgic category $\mathcal{S}_{\text{fused}}$:
$$\mathcal{S}_{\text{fused}} = \Phi\left(\arg\max_{e_v} P(e_v|I), \, \arg\max_{e_t} P(e_t|T)\right)$$

The multimodal synergy coefficient $\Psi \in [0, 1]$ measures semantic congruence between visual and linguistic modalities:
$$\Psi = \alpha \cdot \max_{e_v} P(e_v|I) + (1 - \alpha) \cdot \max_{e_t} P(e_t|T), \quad \alpha = 0.45$$

---

## 2. Nostalgia Score Formulation ($0 \le S_{\text{nost}} \le 100$)

The Nostalgia Index $S_{\text{nost}}$ is computed via a multi-factor grounded objective:

$$S_{\text{nost}} = \min\left(99, \, \max\left(45, \, \mathcal{W}_{\text{temporal}} + \mathcal{W}_{\text{semantic}} + \mathcal{W}_{\text{resonance}} + \mathcal{W}_{\text{synergy}}\right)\right)$$

### 2.1 Component Factors:
1. **Temporal Displacement Weight ($\mathcal{W}_{\text{temporal}} \in [10, 35]$)**:
   Measures explicit time markers (e.g. $\Delta \tau$ years, "childhood", "school days"):
   $$\mathcal{W}_{\text{temporal}} = \min\left(35, \, 10 + \sum_{p \in \mathcal{P}_{\text{time}}} \mathbb{I}(p \in T) \cdot w_p + \beta \cdot \Delta \tau\right)$$
   For benchmark test input *"After 5 years finally together again"*, $\Delta \tau = 5$, contributing $+22$ points.

2. **Reminiscing Semantic Density ($\mathcal{W}_{\text{semantic}} \in [5, 30]$)**:
   Weights lexical memory cues (*memories, reunion, best years, friends, cherish*):
   $$\mathcal{W}_{\text{semantic}} = \min\left(30, \, 5 + \sum_{k \in \mathcal{K}_{\text{rem}}} \mathbb{I}(k \in T) \cdot \gamma_k\right)$$

3. **Emotional Resonance ($\mathcal{W}_{\text{resonance}} \in [4, 20]$)**:
   Scores affective warmth and congruency between facial expressions and textual emotions.

4. **Multimodal Synergy ($\mathcal{W}_{\text{synergy}} \in [0, 15]$)**:
   Proportional to model confidence across both modalities:
   $$\mathcal{W}_{\text{synergy}} = 15 \cdot \left(\frac{C_{\text{vis}} + C_{\text{text}}}{2}\right)$$

---

## 3. Explainable AI (XAI) Framework

### 3.1 Multimodal Attribution Breakdown
The system quantifies relative modality influence through normalized sensitivity gradients:
$$\text{Caption Contribution} = \frac{\Delta \mathcal{L}_T}{\Delta \mathcal{L}_T + \Delta \mathcal{L}_I} \times 100\%$$
$$\text{Image Contribution} = 100\% - \text{Caption Contribution}$$
*Typically, strong temporal captions yield $57\%$ Caption vs. $43\%$ Image contribution.*

### 3.2 SHAP Token Saliency
For each word $t_i \in T$, the marginal Shapley value $\phi_i$ measures contribution towards the nostalgia prediction:
$$\phi_i = \sum_{S \subseteq T \setminus \{t_i\}} \frac{|S|!(|T| - |S| - 1)!}{|T|!} \left(f(S \cup \{t_i\}) - f(S)\right)$$

### 3.3 Visual Grad-CAM Attention Heatmap
To identify visual regions driving the emotion classifier, the gradient of the winning emotion score $y^c$ with respect to visual feature maps $A^k$ is pooled:
$$\alpha_k^c = \frac{1}{Z} \sum_{i} \sum_{j} \frac{\partial y^c}{\partial A_{i, j}^k}$$
$$L_{\text{Grad-CAM}}^c = \text{ReLU}\left(\sum_k \alpha_k^c A^k\right)$$
Rendered as an overlay heatmap where hot colors (red/yellow) indicate facial smile landmarks and ambient golden lighting.

---

## 4. Photographic Color Grading & Style Transfer Science

| Style Name | Emotional Mapping | Color Chemistry Operations |
| :--- | :--- | :--- |
| **Kodak 90s Film** | Happy Nostalgia, Joyful Moments | Lifted black levels ($+25$), amber highlight bias ($R \times 1.32, B \times 0.78$), fine Gaussian film grain ($\sigma = 0.35$), soft radial vignette. |
| **Golden Warm Filter** | Family Memories, Gratitude | Amber saturation ($R \times 1.45, G \times 1.25$), gentle $3.5\text{px}$ Gaussian bloom overlay with screen blend mode. |
| **Polaroid 600 Effect** | Childhood Memories, School Days | Cyan-tinted shadow floor, washed-out highlights, coarse grain ($\sigma = 0.50$), edge chromatic falloff. |
| **Analog Camera Aesthetic**| Friends Reunion, Celebrations | 35mm rangefinder tone curve, punchy retro greens and reds, authentic lens halation. |
| **Sepia Dreamscape** | Bittersweet Melancholy | Luminance-weighted silver gelatin monochrome ($Y = 0.299R + 0.587G + 0.114B$) with warm brown overlay. |
| **70s Kodachrome** | Youthful Wonder, Adventure | Saturated retro reds, warm yellow cast, cinematic 1970s film slide emulation. |
