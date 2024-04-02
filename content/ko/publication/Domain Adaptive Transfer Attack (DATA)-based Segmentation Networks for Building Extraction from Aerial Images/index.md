---
title: 'Domain Adaptive Transfer Attack (DATA)-based Segmentation Networks for Building Extraction from Aerial Images'

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here
# and it will be replaced with their full name and linked to their profile.
authors:
  - 나영환
  - 김준희
  - 이경수
  - 박주흠
  - 황재윤
  - 최지환

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
date: '2020-07-31'
doi: 'https://doi.org/10.1109/TGRS.2020.3010055'

# Schedule page publish date (NOT publication's date).
publishDate: '2020-07-31'

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ['article-journal']

# Publication name and optional abbreviated publication name.
publication: IEEE Transactions on Geoscience and Remote Sensing
publication_short: IEEE Transactions on Geoscience and Remote Sensing (TGRS)  [__SCI(E) IF=5.60, 5.11% (Q1)__]

abstract: Semantic segmentation models based on convolutional neural networks (CNNs) have gained much attention in relation to remote sensing and have achieved remarkable performance for the extraction of buildings from high-resolution aerial images. However, the issue of limited generalization for unseen images remains. When there is a domain gap between the training and test data sets, the CNN-based segmentation models trained by a training data set fail to segment buildings for the test data set. In this article, we propose segmentation networks based on a domain adaptive transfer attack (DATA) scheme for building extraction from aerial images. The proposed system combines the domain transfer and the adversarial attack concepts. Based on the DATA scheme, the distribution of the input images can be shifted to that of the target images while turning images into adversarial examples against a target network. Defending adversarial examples adapted to the target domain can overcome the performance degradation due to the domain gap and increase the robustness of the segmentation model. Cross-data set experiments and ablation study are conducted for three different data sets- the Inria aerial image labeling data set, the Massachusetts building data set, and the WHU East Asia data set. Compared with the performance of the segmentation network without the DATA scheme, the proposed method shows improvements in the overall intersection over union (IoU). Moreover, it is verified that the proposed method outperforms even when compared with feature adaptation (FA) and output space adaptation (OSA).

# Summary. An optional shortened abstract.
# summary: Semantic segmentation models based on convolutional neural networks (CNNs) have gained much attention in relation to remote sensing and have achieved remarkable performance for the extraction of buildings from high-resolution aerial images. However, the issue of limited generalization for unseen images remains. When there is a domain gap between the training and test data sets, the CNN-based segmentation models trained by a training data set fail to segment buildings for the test data set. In this article, we propose segmentation networks based on a domain adaptive transfer attack (DATA) scheme for building extraction from aerial images. The proposed system combines the domain transfer and the adversarial attack concepts. Based on the DATA scheme, the distribution of the input images can be shifted to that of the target images while turning images into adversarial examples against a target network. Defending adversarial examples adapted to the target domain can overcome the performance degradation due to the domain gap and increase the robustness of the segmentation model. Cross-data set experiments and ablation study are conducted for three different data sets- the Inria aerial image labeling data set, the Massachusetts building data set, and the WHU East Asia data set. Compared with the performance of the segmentation network without the DATA scheme, the proposed method shows improvements in the overall intersection over union (IoU). Moreover, it is verified that the proposed method outperforms even when compared with feature adaptation (FA) and output space adaptation (OSA).

tags: []

# Display this page in the Featured widget?
featured: true

# Custom links (uncomment lines below)
# links:
# - name: Custom Link
#   url: http://example.org

# url_pdf: '{{url_pdf}}'
# url_code: '{{url_code}}''
# url_dataset: '{{url_dataset}}'
# url_poster: '{{url_poster}}'
# url_project: ''
# url_slides: ''
# url_source: '{{url_source}}'
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
