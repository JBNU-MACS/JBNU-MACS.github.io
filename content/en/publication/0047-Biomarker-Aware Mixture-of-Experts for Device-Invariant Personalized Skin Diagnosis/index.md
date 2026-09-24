---
title: 'Biomarker-Aware Mixture-of-Experts for Device-Invariant Personalized Skin Diagnosis'

authors:
  - Seo-Yeon Choi
  - Kyungsu Lee

author_notes:
  - ''
  - 'Corresponding author'

date: '2026-09-22T00:00:00+09:00'
doi: ''
publishDate: '2026-09-22T00:00:00+09:00'

publication_types:
  - paper-csai

badges:
  - Top
  - BK/CS
highlight: true

publication: Asian Conference on Computer Vision 2026
publication_short: ACCV2026

abstract: >-
  Smartphone-based skin analysis is limited by device heterogeneity, uncontrolled illumination, and subject-specific variability, yet existing methods treat calibration, domain adaptation, and multi-task prediction in isolation without capturing the causal structure underlying biomarker interactions. We propose an end-to-end framework for device-invariant skin diagnosis built on three principles: (i) hierarchical hybrid normalization formulated as a causal intervention to disentangle diagnostic signals from device-induced nuisance, (ii) a keypoint-guided Skin Mixture-of-Experts that organizes experts around dermatological biomarkers with conditional routing, and (iii) a causal expert deliberation module that enables experts to exchange evidence through clinically motivated dependency constraints, moving beyond simple expert averaging to structured causal reasoning over multi-biomarker outputs. Experiments on multiple public dermatology benchmarks demonstrate consistent improvements over strong 2024--2025 vision and medical foundation baselines.

summary: ___ACCV2026___ <br> _Asian Conference on Computer Vision 2026_

tags: ['AI', 'medical imaging', 'skin diagnosis', 'causal expert deliberation', 'mixture-of-experts', 'device invariance']
featured: true

url_code: ''
url_project: ''
url_source: 'https://openreview.net/revisions?id=ZUcq0XTmMG'
---

### Framework Overview

[![Skin diagnosis framework combining hierarchical hybrid normalization, keypoint-guided Skin Mixture-of-Experts, and biomarker-aware aggregation.](featured.png)](featured.png)

*Figure 1 from the paper. The framework combines device and illumination normalization, biomarker-specific expert routing, and clinically constrained evidence aggregation for personalized skin diagnosis.*
