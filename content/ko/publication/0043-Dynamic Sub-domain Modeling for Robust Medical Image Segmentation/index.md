---
title: 'Dynamic Sub-domain Modeling for Robust Medical Image Segmentation'

authors:
  - Kyungsu Lee
  - seoyeonchoi
  - Jae Youn Hwang
  - Jong-Hye Woo

author_notes:
  - ''
  - ''
  - ''
  - ''

date: '2026-06-11T00:00:00+09:00'
doi: ''
publishDate: '2026-06-11T00:00:00+09:00'

publication_types:
  - conference-international
highlight: true

publication: Medical Image Computing and Computer Assisted Intervention 2026
publication_short: MICCAI 2026

abstract: >-
  Intra-domain distribution shifts are common in medical image segmentation due to variations in acquisition protocols, reconstruction settings, and anatomical morphology, even when data originate from the same nominal domain. We propose a fully automatic segmentation framework that explicitly models latent sub-domains without gradient-based adaptation at inference. Our method dynamically discovers sub-domains via a nonparametric prototype mechanism, expanding only when novel distributional modes are detected. Each prototype conditions a specialized expert via a hypernetwork, forming a prototype-conditioned expert field over the latent manifold. Soft routing with uncertainty-based temperature scaling enables parameter-free test-time adaptation by calibrating sub-domain posteriors without updating model weights. Experiments on 2D medical benchmarks demonstrate improved robustness and granular segmentation accuracy under intra-domain shifts.

summary: ___MICCAI 2026 Early Accept; Top 9%___ <br> _Medical Image Computing and Computer Assisted Intervention 2026_

tags: ['AI', 'medical imaging', 'segmentation', 'domain shift', 'test-time adaptation', 'uncertainty']
featured: true

url_code: ''
url_project: ''
url_source: ''
---
