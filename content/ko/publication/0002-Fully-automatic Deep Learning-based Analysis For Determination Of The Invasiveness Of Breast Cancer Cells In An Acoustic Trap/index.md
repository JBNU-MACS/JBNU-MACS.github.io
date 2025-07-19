---
title: 'Fully-automatic Deep Learning-based Analysis for Determination of the Invasiveness of Breast Cancer Cells in an Acoustic Trap'

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here
# and it will be replaced with their full name and linked to their profile.
authors:
  - 윤상연
  - 이경수
  - 손지훈
  - 양인환
  - Jae Youn Hwang

# Author notes (optional)
author_notes:
  - 'Equal contribution'
  - 'Equal contribution'
  - ''
  - ''
  - ''
  - 'Corresponding author'
# {{equal}}

# date format: '2013-07-01T00:00:00Z'
date: '2020-05-11'
doi: 'https://doi.org/10.1364/BOE.390558'

# Schedule page publish date (NOT publication's date).
publishDate: '2020-05-11'

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ['article-journal']

# Publication name and optional abbreviated publication name.
publication: Biomedical Optics Express
publication_short: Biomedical Optics Express (BOE)  [__SCI(E); IF=3.73, 22.73% (Q1)__]

abstract: A single-beam acoustic trapping technique has been shown to be very useful for determining the invasiveness of suspended breast cancer cells in an acoustic trap with a manual calcium analysis method. However, for the rapid translation of the technology into the clinic, the development of an efficient/accurate analytical method is needed. We, therefore, develop a fully-automatic deep learning-based calcium image analysis algorithm for determining the invasiveness of suspended breast cancer cells using a single-beam acoustic trapping system. The algorithm allows to segment cells, find trapped cells, and quantify their calcium changes over time. For better segmentation of calcium fluorescent cells even with vague boundaries, a novel deep learning architecture with multi-scale/multi-channel convolution operations (MM-Net) is devised and constructed by a target inversion training method. The MM-Net outperforms other deep learning models in the cell segmentation. Also, a detection/quantification algorithm is developed and implemented to automatically determine the invasiveness of a trapped cell. For the evaluation of the algorithm, it is applied to quantify the invasiveness of breast cancer cells. The results show that the algorithm offers similar performance to the manual calcium analysis method for determining the invasiveness of cancer cells, suggesting that it may serve as a novel tool to automatically determine the invasiveness of cancer cells with high-efficiency.

# Summary. An optional shortened abstract.
summary: ___SCI(E); IF=3.73, 22.73% (Q1)___ <br> _Biomedical Optics Express (BOE, 2020, Vol. 11, Issue 6, pp. 2976-2995)_

tags: ['AI', 'biomedical', 'cell', 'tracking', 'segmentation', 'Q1']

# Display this page in the Featured widget?
featured: true

# Custom links (uncomment lines below)
# links:
# - name: Custom Link
#   url: http://example.org

# url_pdf: '{{url_pdf}}'
url_code: ''
# url_dataset: '{{url_dataset}}'
# url_poster: '{{url_poster}}'
# url_project: ''
# url_slides: ''
url_source: 'https://doi.org/10.1364/BOE.390558'
# url_video: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# image:
#   caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/pLCdAaMFLTE)'
#   focal_point: ''
#   preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
# projects:
#   - example

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
# slides: example
---
