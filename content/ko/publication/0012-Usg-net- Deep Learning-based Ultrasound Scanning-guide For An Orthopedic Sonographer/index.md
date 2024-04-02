---
title: 'USG-Net: Deep Learning-based Ultrasound Scanning-Guide for an Orthopedic Sonographer'

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here
# and it will be replaced with their full name and linked to their profile.
authors:
  - 이경수
  - 양재승
  - 이문환
  - 장진호
  - 김준영
  - 황재윤

# Author notes (optional)
author_notes:
  - 'Equal contribution'
  - 'Equal contribution'
  - ''
  - ''
  - 'Corresponding author'
  - 'Corresponding author'
# {{equal}}

# date format: '2013-07-01T00:00:00Z'
date: '2022-09-17'
doi: 'https://doi.org/10.1007/978-3-031-16449-1_3'

# Schedule page publish date (NOT publication's date).
publishDate: '2022-09-17'

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ['paper-conference']

# Publication name and optional abbreviated publication name.
publication: International Conference on Medical Image Computing and Computer-Assisted Intervention
publication_short: International Conference on Medical Image Computing and Computer-Assisted Intervention (MICCAI)  [__Top AI & CV Conference__]

abstract: Ultrasound (US) imaging is widely used in the field of medicine. US images containing pathological information are essential for better diagnosis. However, it is challenging to obtain informative US images because of their anatomical complexity, which is significantly dependent on the expertise of the sonographer. Therefore, in this study, we propose a fully automatic scanning-guide algorithm that assists unskilled sonographers in acquiring informative US images by providing accurate directions of probe movement to search for target disease regions. The main contributions of this study are- (1) proposing a new scanning-guide task that searches for a rotator cuff tear (RCT) region using a deep learning-based algorithm, i.e., ultrasound scanning-guide network (USG-Net); (2) constructing a dataset to optimize the corresponding deep learning algorithm. Multidimensional US images collected from 80 patients with RCT were processed to optimize the scanning-guide algorithm which classified the existence of RCT. Furthermore, the algorithm provides accurate directions for the RCT, if it is not in the current frame. The experimental results demonstrate that the fully optimized scanning-guide algorithm offers accurate directions to localize a probe within target regions and helps to acquire informative US images.

# Summary. An optional shortened abstract.
summary: ___MICCAI 2022 (Top AI & CV Conference)___ <br> _International Conference on Medical Image Computing and Computer-Assisted Intervention2022_

tags: []

# Display this page in the Featured widget?
featured: true

# Custom links (uncomment lines below)
# links:
# - name: Custom Link
#   url: http://example.org

# url_pdf: '{{url_pdf}}'
url_code: 'https://github.com/kyungsu-lee-ksl/USG-Net'
# url_dataset: '{{url_dataset}}'
# url_poster: '{{url_poster}}'
# url_project: ''
# url_slides: ''
url_source: 'https://doi.org/10.1007/978-3-031-16449-1_3'
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
