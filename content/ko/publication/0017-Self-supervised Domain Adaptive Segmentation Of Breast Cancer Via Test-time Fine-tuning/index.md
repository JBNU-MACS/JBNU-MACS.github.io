---
title: 'Self-supervised Domain Adaptive Segmentation Of Breast Cancer Via Test-time Fine-tuning'

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here
# and it will be replaced with their full name and linked to their profile.
authors:
  - 이경수
  - 이해윤
  - Georges El Fakhri
  - Jonghye Woo
  - 황재윤

# Author notes (optional)
author_notes:
  - ''
  - ''
  - ''
  - 'Corresponding author'
  - 'Corresponding author'
# {{equal}}

# date format: '2013-07-01T00:00:00Z'
date: '2023-10-01'
doi: 'https://doi.org/10.1007/978-3-031-43907-0_52'

# Schedule page publish date (NOT publication's date).
publishDate: '2023-10-01'

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ['paper-conference']

# Publication name and optional abbreviated publication name.
publication: International Conference on Medical Image Computing and Computer-Assisted Intervention
publication_short: International Conference on Medical Image Computing and Computer-Assisted Intervention (MICCAI)  [__Top AI & CV Conference__]

abstract: Unsupervised domain adaptation (UDA) has become increasingly popular in imaging-based diagnosis due to the challenge of labeling a large number of datasets in target domains. Without labeled data, well-trained deep learning models in a source domain may not perform well when applied to a target domain. UDA allows for the use of large-scale datasets from various domains for model deployment, but it can face difficulties in performing adaptive feature extraction when dealing with unlabeled data in an unseen target domain. To address this, we propose an advanced test-time fine-tuning UDA framework designed to better utilize the latent features of datasets in the unseen target domain by fine-tuning the model itself during diagnosis. Our proposed framework is based on an auto-encoder-based network architecture that fine-tunes the model itself. This allows our framework to learn knowledge specific to the unseen target domain during the fine-tuning phase. In order to further optimize our framework for the unseen target domain, we introduce a re-initialization module that injects randomness into network parameters. This helps the framework to converge to a local minimum that is better-suited for the target domain, allowing for improved performance in domain adaptation tasks. To evaluate our framework, we carried out experiments on UDA segmentation tasks using breast cancer datasets acquired from multiple domains. Our experimental results demonstrated that our framework achieved state-of-the-art performance, outperforming other competing UDA models, in segmenting breast cancer on ultrasound images from an unseen domain, which supports its clinical potential for improving breast cancer diagnosis.


# Summary. An optional shortened abstract.
summary: __MICCAI2023 (Top AI & CV Conference)__ <br> International Conference on Medical Image Computing and Computer-Assisted Intervention2023 <br><br>

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
url_source: 'https://doi.org/10.1007/978-3-031-43907-0_52'
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
