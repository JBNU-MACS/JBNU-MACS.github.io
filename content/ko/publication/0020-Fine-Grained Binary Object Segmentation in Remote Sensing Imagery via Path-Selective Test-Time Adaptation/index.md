---
title: 'Fine-Grained Binary Object Segmentation in Remote Sensing Imagery via Path-Selective Test-Time Adaptation'

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here
# and it will be replaced with their full name and linked to their profile.
authors:
  - Kyungsu Lee
  - Haeyun Lee
  - 박주흠
  - Jae Youn Hwang

# Author notes (optional)
author_notes:
  - ''
  - ''
  - ''
  - 'Corresponding author'
# {{equal}}

# date format: '2013-07-01T00:00:00Z'
date: '2024-03-20'
doi: 'https://doi.org/10.1109/TGRS.2024.3378311'

# Schedule page publish date (NOT publication's date).
publishDate: '2024-03-20'

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ['article-journal']

# Publication name and optional abbreviated publication name.
publication: IEEE Transactions on Geoscience and Remote Sensing
publication_short: TGRS
journal_type: SCI(E)
impact_factor: '8.20'
jcr_rank: '5.20%'
jcr_percentile: 'Q1'

abstract: For several decades, the significance of geospatial object segmentation in remote sensing (RS) images has been emphasized for both scientific and industrial purposes. Object segmentation plays a pivotal role in the analysis of urban and rural area expansion, as well as in advancing sustainable development within the realm of RS. Deep learning (DL)-based segmentation methodologies, overcoming the limitations of the conventional vision-based analysis, have yielded precise predictions by utilizing convolutional neural networks (CNNs). However, CNNs classify images at the pixel level and generate outputs based on probability distributions derived from the SoftMax function. This approach precludes the reflection of morphological properties, such as shape and object density, during predictions in RS imagery, leading to imprecise results. In addition, due to the intrinsic attributes of probability-based segmentation, fine-grained segmentation may not be achieved, leading to coarse predictions in the boundaries of geospatial objects. To address this issue, this article introduces a novel DL framework, the density-based guide network (DG-Net), which incorporates the density of segmentation targets into pixel-wise classification through a test-time adaptation learning methodology. DG-Net first discerns the density of segmentation targets in the input images, then fine-tunes the baseline network to reflect this density, thereby generating precise segmentation outputs. The effectiveness of DG-Net is demonstrated through various multitarget segmentation benchmarks in RS imagery. Experimental results demonstrate the superior performance of the DG-Net in object segmentation when compared to state-of-the-art (SotA) models across numerous aerial image and satellite image datasets.

# Summary. An optional shortened abstract.
summary: ___SCI(E); IF=8.20, 5.20% (Q1)___ <br> _IEEE Transactions on Geoscience and Remote Sensing (TGRS, 2024, Vol. 62)_

tags: ['AI', 'remote sensing', 'Fine-Tuning', 'Segmentation', 'Test-Time Adaptation', 'Q1']

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
url_source: 'https://doi.org/10.1109/TGRS.2024.3378311'
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
