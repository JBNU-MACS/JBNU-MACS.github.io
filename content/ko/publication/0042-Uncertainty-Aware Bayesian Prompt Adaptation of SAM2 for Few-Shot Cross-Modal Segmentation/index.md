---
title: 'Uncertainty-Aware Bayesian Prompt Adaptation of SAM2 for Few-Shot Cross-Modal Segmentation'

authors:
  - 홍사강
  - Jong Pil Yoon
  - Jun-Young Kim
  - Kyungsu Lee

author_notes:
  - ''
  - ''
  - ''
  - 'Corresponding author'

date: '2026-06-07'
doi: ''
publishDate: '2026-06-07'

publication_types: ['article-journal']

publication: Expert Systems With Applications
publication_short: ESWA
journal_type: SCI(E)
impact_factor: '9.4'
jcr_rank: '5%'
jcr_percentile: 'Q1'

abstract: >-
  Medical image segmentation is essential for clinical image analysis, supporting diagnosis, quantitative assessment, treatment planning, and follow-up evaluation. In real-world clinical workflows, the same anatomical or pathological target may be examined using different imaging modalities, whose distinct signal properties and appearance distributions make reliable cross-modality segmentation challenging. Foundation segmentation models such as the Segment Anything Model (SAM) have demonstrated strong generalization on large-scale natural images. However, reliable adaptation to medical imaging remains challenging due to severe cross-modality shifts, limited annotations, and modality-specific uncertainty. Few-shot cross-modality medical image segmentation often suffers from unstable convergence and overconfident predictions, undermining reliability in clinical decision-making. This study aims to alleviate these challenges by explicitly modeling task-level uncertainty during adaptation. We re-interpret few-shot cross-modality medical image segmentation as a task-level uncertainty inference problem, and we propose BayesPrompt, an uncertainty-aware Bayesian prompt adaptation framework for foundation segmentation models. BayesPrompt incorporates a probabilistic prompt module that encodes feature statistics and task-level uncertainty from few-shot support sets and injects them into the decoder attention of SAM2 while freezing the backbone encoder. Additionally, we introduce Bayesian Meta-Prior Adaptation, which stabilizes few-shot adaptation by aligning target-domain posteriors with source-domain meta-priors via lightweight decoder-head updates. The proposed method is evaluated on ultrasound and magnetic resonance imaging (MRI) datasets under both single-modality and cross-modality segmentation settings. Experimental results show that BayesPrompt consistently outperforms deterministic prompt tuning and adaptation baselines, yielding improved segmentation accuracy, enhanced robustness to modality shifts, and more reliable uncertainty calibration across all evaluated scenarios. These findings demonstrate the importance of modeling task-level uncertainty for few-shot cross-modality adaptation of foundation segmentation models in the evaluated retrospective setting, while external multi-center validation and prospective reader studies remain necessary before any clinical deployment claim can be made.

summary: ___SCI(E); IF=9.4, 5% (Q1)___ <br> _Expert Systems With Applications (2026년 6월 7일 Accept)_

tags: ['AI', 'medical imaging', 'few-shot', 'cross-modal segmentation', 'SAM2', 'bayesian adaptation', 'uncertainty']

featured: true

url_project: ''
url_source: ''
---
