# License and rights review (initial)

This is a screening record, not legal advice or permission to use content.

| Resource | Verified information | Current decision |
|---|---|---|
| EmoSet | Official project describes EmoSet-3.3M and an EmoSet-118K human/machine-labeled subset with eight emotion classes and six attributes. Repository exposes an MIT license for its code. That does not establish rights to image files. | Do not download or integrate until image provenance, access terms, license, size and permitted research use are documented from the official dataset access route. Prefer a tiny authorized subset only after audit. |
| AVA | CVPR 2012 dataset; metadata and images originate from DPChallenge. A mirrored dataset README explicitly says image copyright remains with photographers/DPChallenge. Approximate 30–32 GB full-image archive figures found on third-party mirrors are not official size/availability guarantees. | Do not download images. Determine whether metadata-only or individually accessible material is permitted; obtain rights/access clarification first. |
| GoEmotions | Google Research describes 58,009 Reddit comments with 27 emotion labels plus neutral, with documented train/validation/test splits. It is text data, not image-caption pairs. | Optional, text-only baseline. Confirm repository/data license and Reddit-derived data use terms before acquisition. |
| User preference data | No dataset exists. Proposed pairwise record schema is in `src/memoreel/preference/schema.py`. | No collection until ethics review, consent language, retention/deletion process, and participant recruitment protocol are approved. |
| CLIP / diffusion checkpoints | No checkpoint selected or downloaded. Model weights have their own license/terms. | Recheck exact checkpoint, adapter compatibility, and usage rights before any integration. |

Sources: [EmoSet official repository](https://github.com/JingyuanYY/EmoSet), [EmoSet ICCV paper](https://openaccess.thecvf.com/content/ICCV2023/papers/Yang_EmoSet_A_Large-scale_Visual_Emotion_Dataset_with_Rich_Attributes_ICCV_2023_paper.pdf), [AVA paper](https://refbase.cvc.uab.es/files/MMP2012a.pdf), [AVA image-rights note in dataset README](https://github.com/ylogx/aesthetics/blob/master/data/ava/README.txt), [Google Research GoEmotions](https://github.com/google-research/google-research/tree/master/goemotions).
