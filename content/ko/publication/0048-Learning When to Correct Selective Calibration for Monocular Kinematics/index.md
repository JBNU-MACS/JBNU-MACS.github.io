---
title: 'Learning When to Correct: Selective Calibration for Monocular Kinematics'

authors:
  - Jun Ho Lee
  - Dongjun Kang
  - Kyungsu Lee

date: '2027-01-01T00:00:00+09:00'
doi: ''
publishDate: '2026-10-15T00:00:00+09:00'

publication_types:
  - paper-csai

highlight: true
publication: IEEE/CVF Winter Conference on Applications of Computer Vision 2027
publication_short: WACV2027

abstract: >-
  Post hoc calibration of markerless kinematics enables accessible movement analysis from monocular video, but conventional pipelines apply corrections unconditionally, regardless of initial estimate fidelity. Across 82 subjects, four capture domains, four pose estimators, and nine correction paradigms (3.48M evaluations), we show that Extremely Randomized Trees (ExtraTrees) outperform deep tabular, generative, and temporal alternatives in predicting kinematic residuals from 21 dimensional biomechanical biomarkers, reducing macro MAE from 12.54° to 6.22° (50.4%). Despite this improvement, unconditional ExtraTrees exhibits a critical overcorrection dilemma, pushing 34.7% of frames initially within a 5° tolerance outside the tolerance and producing a 76.8% preservation failure rate at 2°. Factorial transfer analysis further shows that changing the upstream pose estimator induces a domain shift comparable to changing the physical capture environment (-1.76° versus -1.32°). To address this problem, we extract an eight dimensional forest consensus representation from tree variance, prediction quantiles, and leaf topology to decide whether to preserve the incumbent estimate or adopt the ExtraTrees candidate. Trained via nested out of fold benefit regression, our reference free selective router reduces macro MAE to 5.94°, lowers preservation failure from 34.7% to 16.5%, and outperforms unconditional ExtraTrees in 15 of 16 domain and estimator combinations.

summary: '___WACV2027___ <br> _IEEE/CVF Winter Conference on Applications of Computer Vision 2027_ <br> Undergraduate first-author research'

tags: ['AI', 'computer vision', 'monocular kinematics', 'selective calibration', 'undergraduate research']
featured: true

url_pdf: 'https://openreview.net/pdf?id=jWI5vidCGy'
url_source: 'https://openreview.net/forum?id=jWI5vidCGy'
url_code: ''
url_project: ''
---

**이준호 학부연구생이 제1저자로 수행한 연구**로, **WACV 2027 Applications Track**에 채택되었습니다. 저자는 이준호, 강동준, 이경수입니다.

단안 영상 기반 관절 운동학 추정에서 이미 정확한 추정값까지 보정해 오히려 오차를 키우는 과보정 문제를 다룹니다. 제안한 선택적 보정 기법은 기존 추정값을 유지할지 ExtraTrees 보정값을 채택할지 판단하여, 평균 절대 오차를 **5.94°**로 줄이고 5° 허용 범위 내 추정값의 보존 실패율을 **34.7%에서 16.5%**로 낮췄습니다.

### 선택적 보정 프레임워크

[![기존 추정값과 ExtraTrees 보정값 사이에서 선택하는 보존 중심 선택적 보정 프레임워크.](featured.png)](featured.png)

*논문 Figure 2. 피험자 단위로 분리된 학습과 forest consensus 표현을 이용해 보정의 이득을 예측하며, 추론 시 참조 측정값 없이 보정 여부를 결정합니다.*
