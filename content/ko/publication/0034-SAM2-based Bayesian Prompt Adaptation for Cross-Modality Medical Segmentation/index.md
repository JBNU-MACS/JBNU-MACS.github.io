---
title: 'SAM2-based Bayesian Prompt Adaptation for Cross-Modality Medical Segmentation'

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here
# and it will be replaced with their full name and linked to their profile.
authors:
  - 홍사강
  - Jun-Yung Kim
  - Kyungsu Lee

# Author notes (optional)
author_notes:
  - ''
  - ''
  - 'Corresponding author'
# {{equal}}

# date format: '2013-07-01T00:00:00Z'
date: '2025-11-07'
doi: ''

# Schedule page publish date (NOT publication's date).
publishDate: '2025-11-07'

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types:
  - conference-domestic

# Publication name and optional abbreviated publication name.
publication: 대한의용생체공학회 2025 추계학술대회
publication_short: KOSOMBE2025 Fall

abstract: Segmentation foundation models such as SAM2 generalize well in natural images, but adapting them to medical imaging remains challenging because of cross-modality gaps and limited annotations. We propose BayesPrompt, a SAM2-based Bayesian Prompt Adaptation framework for few-shot medical segmentation. BayesPrompt combines Bayesian meta-prior adaptation, which regularizes lightweight head updates through source-target posterior alignment, with a probabilistic prompt module that encodes support-set feature statistics and uncertainty into decoder prompts. Experiments on ultrasound and MRI show improvements in few-shot generalization, calibration, and efficiency over existing adaptation baselines.

# Summary. An optional shortened abstract.
summary: ___KOSOMBE 2025 Fall___ <br> _대한의용생체공학회 2025 추계학술대회 (Poster 247)_

tags: ['AI', 'medical', 'few-shot', 'segmentation', 'SAM2', 'bayesian adaptation']

# Display this page in the Featured widget?
featured: false

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
url_source: 'https://www.kosombe.or.kr/register/2025_fall/program/sub07.html'
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
