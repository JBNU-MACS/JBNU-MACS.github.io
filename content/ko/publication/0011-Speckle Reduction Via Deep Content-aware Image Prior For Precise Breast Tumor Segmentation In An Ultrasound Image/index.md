---
title: 'Speckle Reduction Via Deep Content-aware Image Prior For Precise Breast Tumor Segmentation In An Ultrasound Image'

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here
# and it will be replaced with their full name and linked to their profile.
authors:
  - 이해윤
  - 이문환
  - 윤상연
  - 이경수
  - 류하민
  - 황재윤

# Author notes (optional)
author_notes:
  - ''
  - ''
  - ''
  - ''
  - ''
  - 'Corresponding author'
# {{equal}}

# date format: '2013-07-01T00:00:00Z'
date: '2022-07-25'
doi: 'https://doi.org/10.1109/TUFFC.2022.3193640'

# Schedule page publish date (NOT publication's date).
publishDate: '2022-07-25'

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ['article-journal']

# Publication name and optional abbreviated publication name.
publication: IEEE Transactions on Ultrasonics,  Ferroelectrics,  and Frequency Control
publication_short: IEEE Transactions on Ultrasonics,  Ferroelectrics,  and Frequency Control (TUFFC)  [__SCI(E); IF=3.60, 17.70% (Q1)__]

abstract: The performance of computer-aided diagnosis (CAD) systems that are based on ultrasound imaging has been enhanced owing to the advancement in deep learning. However, because of the inherent speckle noise in ultrasound images, the ambiguous boundaries of lesions deteriorate and are difficult to distinguish, resulting in the performance degradation of CAD. Although several methods have been proposed to reduce speckle noise over decades, this task remains a challenge that must be improved to enhance the performance of CAD. In this article, we propose a deep content-aware image prior (DCAIP) with a content-aware attention module (CAAM) for superior despeckling of ultrasound images without clean images. For the image prior, we developed a CAAM to deal with the content information in an input image. In this module, super-pixel pooling (SPP) is used to give attention to salient regions in an ultrasound image. Therefore, it can provide more content information regarding the input image when compared to other attention modules. The DCAIP consists of deep learning networks based on this attention module. The DCAIP is validated by applying it as a preprocessing step for breast tumor segmentation in ultrasound images, which is one of the tasks in CAD. Our method improved the segmentation performance by 15.89% in terms of the area under the precision_ecall (PR) curve (AUPRC). The results demonstrate that our method enhances the quality of ultrasound images by effectively reducing speckle noise while preserving important information in the image, promising for the design of superior CAD systems.

# Summary. An optional shortened abstract.
summary: __SCI(E); IF=3.60, 17.70% (Q1)__ <br> IEEE Transactions on Ultrasonics,  Ferroelectrics,  and Frequency Control (TUFFC, 2022, Vol. 69, Issue 9, pp. 2638-2650)

tags: []

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
url_source: 'https://doi.org/10.1109/TUFFC.2022.3193640'
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
