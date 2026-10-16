---
title: 'Learning When to Correct: Selective Calibration for Monocular Kinematics'

authors:
  - Jun Ho Lee
  - Dongjun Kang
  - Kyungsu Lee

author_notes:
  - ''
  - ''
  - 'Corresponding author'

date: '2027-01-01T00:00:00+09:00'
doi: ''
publishDate: '2026-10-15T00:00:00+09:00'

publication_types:
  - paper-csai

badges:
  - Top
  - BK/CS
highlight: true
publication: IEEE/CVF Winter Conference on Applications of Computer Vision 2027
publication_short: WACV2027

research_question: "Can video-based movement estimates be corrected more selectively?"
research_overview: "This work learns when to retain a joint-angle estimate and when to apply a correction. It was first-authored by undergraduate researcher Jun Ho Lee."

abstract: >-
  Post hoc calibration of markerless kinematics enables accessible movement analysis from monocular video, but conventional pipelines apply corrections unconditionally, regardless of initial estimate fidelity. Across 82 subjects, four capture domains, four pose estimators, and nine correction paradigms (3.48M evaluations), we show that Extremely Randomized Trees (ExtraTrees) outperform deep tabular, generative, and temporal alternatives in predicting kinematic residuals from 21 dimensional biomechanical biomarkers, reducing macro MAE from 12.54° to 6.22° (50.4%). Despite this improvement, unconditional ExtraTrees exhibits a critical overcorrection dilemma, pushing 34.7% of frames initially within a 5° tolerance outside the tolerance and producing a 76.8% preservation failure rate at 2°. Factorial transfer analysis further shows that changing the upstream pose estimator induces a domain shift comparable to changing the physical capture environment (-1.76° versus -1.32°). To address this problem, we extract an eight dimensional forest consensus representation from tree variance, prediction quantiles, and leaf topology to decide whether to preserve the incumbent estimate or adopt the ExtraTrees candidate. Trained via nested out of fold benefit regression, our reference free selective router reduces macro MAE to 5.94°, lowers preservation failure from 34.7% to 16.5%, and outperforms unconditional ExtraTrees in 15 of 16 domain and estimator combinations.

summary: '___WACV2027___ <br> _IEEE/CVF Winter Conference on Applications of Computer Vision 2027_ <br> Undergraduate first-author research'

tags: ['AI', 'computer vision', 'monocular kinematics', 'selective calibration', 'undergraduate research']
featured: true

url_source: 'https://openreview.net/forum?id=jWI5vidCGy'
url_code: ''
url_project: ''
---

This work, **first-authored by undergraduate researcher Jun Ho Lee**, has been accepted to the **WACV 2027 Main Conference (Application Track)**. The authors are Jun Ho Lee, Dongjun Kang, and Kyungsu Lee.

The proposed selective calibration method learns whether to preserve an existing monocular kinematic estimate or adopt an ExtraTrees correction. It achieves a macro MAE of **5.94°** and reduces preservation failure at a 5° tolerance from **34.7% to 16.5%**.

### Selective Calibration Framework

[![Preservation-aware selective calibration framework choosing between the incumbent estimate and an ExtraTrees correction.](featured.png)](featured.png)

*Figure 2 from the paper. Subject-disjoint training and forest consensus features support benefit prediction, allowing reference-free correction decisions at inference.*
