---
title: 'Uncertainty-Aware Bayesian Prompt Adaptation for Robust Cross-Modality Medical Segmentation'

authors:
  - sakanghong
  - Jun-Young Kim
  - Kyungsu Lee

author_notes:
  - ''
  - ''
  - 'Corresponding author'

date: '2026-06-01T00:00:00+09:00'
doi: ''
publishDate: '2026-06-01T00:00:00+09:00'

publication_types:
  - conference-international
highlight: true

publication: Medical Image Computing and Computer Assisted Intervention 2026
publication_short: MICCAI 2026

abstract: >-
  Segmentation foundation models such as SAM2 generalize well to natural images, yet adapting them to heterogeneous medical modalities remains challenging due to severe domain shifts and scarce annotations. We propose BayesPrompt, a Bayesian prompt adaptation framework for few-shot cross-modality medical segmentation. BayesPrompt combines Bayesian Meta-Prior Adaptation (BMPA), which regularizes lightweight decoder updates via source-target posterior alignment, with a Probabilistic Prompt Module (PPM) that encodes class-wise feature statistics and predictive uncertainty into attention-conditioned prompt tokens. This design supports both gradient-free fast prompting and efficient Bayesian fine-tuning while mitigating overfitting and improving calibration. We evaluate BayesPrompt on ultrasound and MRI rotator cuff tear segmentation under single- and cross-modality transfer with k in {1,3,5,10} labeled target samples. BayesPrompt consistently improves Dice performance and robustness, demonstrating data-efficient adaptation of segmentation foundation models for medical imaging.

summary: ___MICCAI 2026 Early Accept; Top 9%___ <br> _Medical Image Computing and Computer Assisted Intervention 2026_

tags: ['AI', 'medical imaging', 'segmentation', 'SAM2', 'bayesian adaptation', 'uncertainty']
featured: true

url_code: ''
url_project: ''
url_source: ''
---
