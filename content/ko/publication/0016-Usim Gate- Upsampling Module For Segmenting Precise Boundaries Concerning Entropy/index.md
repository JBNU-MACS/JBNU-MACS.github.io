---
title: 'USIM Gate: Upsampling Module for Segmenting Precise Boundaries Concerning Entropy'

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here
# and it will be replaced with their full name and linked to their profile.
authors:
  - Kyungsu Lee
  - Haeyun Lee
  - Jae Youn Hwang

# Author notes (optional)
author_notes:
  - ''
  - ''
  - 'Corresponding author'
# {{equal}}

# date format: '2013-07-01T00:00:00Z'
date: '2023-04-27'
doi: 'https://proceedings.mlr.press/v206/lee23a.html'

# Schedule page publish date (NOT publication's date).
publishDate: '2023-04-27'

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types:
  - paper-csai

badges:
  - Top
  - BK/CS
highlight: true


# Publication name and optional abbreviated publication name.
publication: Artificial Intelligence and Statistics
publication_short: AISTATS2022

abstract: Deep learning (DL) techniques for precise semantic segmentation have remained a challenge because of the vague boundaries of target objects caused by the low resolution of images. Despite the improved segmentation performance using up/downsampling operations in early DL models, conventional operators cannot fully preserve spatial information and thus generate vague boundaries of target objects. Therefore, for the precise segmentation of target objects in many domains, this paper presents two novel operators- (1) upsampling interpolation method (USIM), an operator that upsamples input feature maps and combines feature maps into one while preserving the spatial information of both inputs, and (2) USIM gate (UG), an advanced USIM operator with boundary-attention mechanisms. We designed our experiments using aerial images where the boundaries critically influence the results. Furthermore, we verified the feasibility that our approach effectively segments target objects using the cityscapes dataset. The experimental results demonstrate that using the USIM and UG with state-of-the-art DL models can improve the segmentation performance with clear boundaries of target objects (Intersection over Union- +6.9; BJ- +10.1). Furthermore, mathematical proofs verify that the USIM and UG contribute to the handling of spatial information.

# Summary. An optional shortened abstract.
summary: ___AISTATS 2023 (Top AI & CV Conference)___ <br> _Artificial Intelligence and Statistics2023_

tags: ['AI', 'remote sensing', 'segmentation', 'localization']

# Display this page in the Featured widget?
featured: true

# Custom links (uncomment lines below)
# links:
# - name: Custom Link
#   url: http://example.org

# url_pdf: '{{url_pdf}}'
url_code: 'https://github.com/kyungsu-lee-ksl/USIM-GATE'
# url_dataset: '{{url_dataset}}'
# url_poster: '{{url_poster}}'
# url_project: ''
# url_slides: ''
url_source: 'https://proceedings.mlr.press/v206/lee23a.html'
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
