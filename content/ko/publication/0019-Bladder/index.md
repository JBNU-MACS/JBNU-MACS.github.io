---
title: 'Intelligent Bladder Volume Monitoring for Wearable Ultrasound Devices: Enhancing Accuracy through Deep Learning-based Coarse-to-Fine Shape Estimation'

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here
# and it will be replaced with their full name and linked to their profile.
authors:
  - Kyungsu Lee
  - Moon Hwan Lee
  - Dongho Kang
  - Sewoong Kim
  - Jin Ho Chang
  - Seung-June Oh
  - Jae Youn Hwang

# Author notes (optional)
author_notes:
  - 'Equal contribution'
  - 'Equal contribution'
  - ''
  - ''
  - ''
  - 'Corresponding author'
  - 'Corresponding author'
# {{equal}}

# date format: '2013-07-01T00:00:00Z'
date: '2024-01-05'
doi: 'https://doi.org/10.1109/TUFFC.2024.3350033'

# Schedule page publish date (NOT publication's date).
publishDate: '2024-01-05'

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ['article-journal']

# Publication name and optional abbreviated publication name.
publication: IEEE Transactions on Ultrasonics, Ferroelectrics, and Frequency Control
publication_short: TUFFC
journal_type: SCI(E)
impact_factor: '3.6'
jcr_rank: '17.70%'
jcr_percentile: 'Q1'

abstract: Accurate and continuous bladder volume monitoring is crucial for managing urinary dysfunctions. Wearable ultrasound devices offer a solution by enabling non-invasive and real-time monitoring. Previous studies have limitations in power consumption and computation cost or quantitative volume estimation capability. To alleviate this, we present a novel pipeline that effectively integrates conventional feature extraction and deep learning to achieve continuous quantitative bladder volume monitoring efficiently. Particularly, in the proposed pipeline, bladder shape is coarsely estimated by a simple bladder wall detection algorithm in wearable devices, and the bladder wall coordinates are wirelessly transferred to an external server. Subsequently, a roughly estimated bladder shape from the wall coordinates is refined in an external server with a diffusion-based model. With this approach, power consumption and computation costs on wearable devices remained low, while fully harnessing the potential of deep learning for accurate shape estimation. To evaluate the proposed pipeline, we collected a dataset of bladder ultrasound images and RF signals from 250 patients. By simulating data acquisition from wearable devices using the dataset, we replicated real-world scenarios and validated the proposed method within these scenarios. Experimental results exhibit superior improvements, including +9.32% of IoU value in 2D segmentation and -22.06 of RMSE in bladder volume regression compared to state-of-the-art performance from alternative methods, emphasizing the potential of this approach in continuous bladder volume monitoring in clinical settings. Therefore, this study effectively bridges the gap between accurate bladder volume estimation and the practical deployment of wearable ultrasound devices, promising improved patient care and quality of life.

# Summary. An optional shortened abstract.
summary: ___SCI(E); IF=3.60, 17.70% (Q1)___ <br> _IEEE Transactions on Ultrasonics, Ferroelectrics, and Frequency Control (TUFFC, 2024, Early Access)_

tags: ['AI', 'medical', 'ultrasound', 'Diffusion', 'Q1']

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
url_source: 'https://doi.org/10.1109/TUFFC.2024.3350033'
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
