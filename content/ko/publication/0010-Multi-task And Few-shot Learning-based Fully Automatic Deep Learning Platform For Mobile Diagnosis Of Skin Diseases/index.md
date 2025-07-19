---
title: 'Multi-task and Few-shot Learning-based Fully Automatic Deep Learning Platform for Mobile Diagnosis of Skin Diseases'

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here
# and it will be replaced with their full name and linked to their profile.
authors:
  - 이경수
  - T C Cavalcanti
  - 김세웅
  - 류하민
  - 서대헌
  - 이동훈
  - Jae Youn Hwang

# Author notes (optional)
author_notes:
  - ''
  - ''
  - ''
  - ''
  - ''
  - 'Corresponding author'
  - 'Corresponding author'
# {{equal}}

# date format: '2013-07-01T00:00:00Z'
date: '2022-07-25'
doi: 'https://doi.org/10.1109/JBHI.2022.3193685'

# Schedule page publish date (NOT publication's date).
publishDate: '2022-07-25'

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ['article-journal']

# Publication name and optional abbreviated publication name.
publication: IEEE Journal of Biomedical and Health Informatics
publication_short: IEEE Journal of Biomedical and Health Informatics (JBHI)  [__SCI(E); IF=7.70, 6.40% (Q1)__]

abstract: Fluorescence imaging-based diagnostic systems have been widely used to diagnose skin diseases due to their ability to provide detailed information related to the molecular composition of the skin compared to conventional RGB imaging. In addition, recent advances in smartphones have made them suitable for application in biomedical imaging, and therefore various smartphone-based optical imaging systems have been developed for mobile healthcare. However, an advanced analysis algorithm is required to improve the diagnosis of skin diseases. Various deep learning-based algorithms have recently been developed for this purpose. However, deep learning-based algorithms using only white-light reflectance RGB images have exhibited limited diagnostic performance. In this study, we developed an auxiliary deep learning network called fluorescence-aided amplifying network (FAA-Net) to diagnose skin diseases using a developed multi-modal smartphone imaging system that offers RGB and fluorescence images. FAA-Net is equipped with a meta-learning-based algorithm to solve problems that may occur due to the insufficient number of images acquired by the developed system. In addition, we devised a new attention-based module that can learn the location of skin diseases by itself and emphasize potential disease regions, and incorporated it into FAA-Net. We conducted a clinical trial in a hospital to evaluate the performance of FAA-Net and to compare various evaluation metrics of our developed model and other state-of-the-art models for the diagnosis of skin diseases using our multi-modal system. Experimental results demonstrated that our developed model exhibited an 8.61% and 9.83% improvement in mean accuracy and area under the curve in classifying skin diseases, respectively, compared with other advanced models.

# Summary. An optional shortened abstract.
summary: ___SCI(E); IF=7.70, 6.40% (Q1)___ <br> _IEEE Journal of Biomedical and Health Informatics (JBHI, 2022, Vol. 27, Issue 1, pp. 176-187)_

tags: ['AI', 'medical', 'healthcare', 'skin', 'few-shot', 'multi-task', 'Q1']

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
url_source: 'https://doi.org/10.1109/JBHI.2022.3193685'
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
