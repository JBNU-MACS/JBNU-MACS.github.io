---
title: 'Predicting Obstructive Sleep Apnea Based on Computed Tomography Scan Using Deep Learning Models'

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here
# and it will be replaced with their full name and linked to their profile.
authors:
  - 김정훈
  - 이경수
  - 김현진
  - 박해찬
  - 황재윤
  - 박석원
  - 공현중
  - 김진엽

# Author notes (optional)
author_notes:
  - 'Equal contribution'
  - 'Equal contribution'
  - ''
  - ''
  - ''
  - ''
  - 'Corresponding author'
  - 'Corresponding author'
# {{equal}}

# date format: '2013-07-01T00:00:00Z'
date: '2024-03-12'
doi: 'https://doi.org/10.1164/rccm.202304-0767OC'

# Schedule page publish date (NOT publication's date).
publishDate: '2024-03-12'

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ['article-journal']

# Publication name and optional abbreviated publication name.
publication: American Journal of Respiratory and Critical Care Medicine
publication_short: American Journal of Respiratory and Critical Care Medicine (AJRCCM)  [__SCI(E); IF=24.70, 3.80% (Q1)__]

abstract: Rationale| The incidence of clinically undiagnosed obstructive sleep apnea (OSA) is high among the general population due to limited access to polysomnography. Computed tomography (CT) of craniofacial regions obtained for other purposes can be beneficial in predicting OSA and its severity. Objectives| To predict OSA and its severity based on paranasal CT using a 3-dimensional deep learning algorithm. Methods| One internal dataset (n=798) and two external datasets (n=135 and 85) were used in this study. In the internal dataset, 92 normal, 159 mild, 201 moderate, and 346 severe OSA participants were enrolled to derive the deep learning model. A multimodal deep learning model was elicited from the connection between a 3-dimensional convolutional neural network (CNN)-based part treating unstructured data (CT images) and a multi-layer perceptron (MLP)-based part treating structured data (age, sex, and body mass index) to predict OSA and its severity. Measurements and Main Results| In four-class classification for predicting the severity of OSA, the AirwayNet-MM-H model (multimodal model with airway-highlighting preprocessing algorithm) showed an average accuracy of 87.6% (95% confidence interval [CI] 86.8–88.6) in the internal dataset and 84.0% (95% CI 83.0–85.1) and 86.3% (95% CI 85.3-87.3) in the two external datasets, respectively. In the two-class classification for predicting significant OSA (moderate to severe OSA), The area under the receiver operating characteristics (AUROC), accuracy, sensitivity, specificity, and F1 score were 0.910 (95% CI 0.899–0.922), 91.0% (95% CI 90.1–91.9), 89.9% (95% CI 88.8–90.9), 93.5% (95% CI 92.7–94.3), and 93.2% (95% CI 92.5–93.9), respectively, in the internal dataset. Furthermore, the diagnostic performance of the Airway Net-MM-H model outperformed that of the other six state-of-the-art deep learning models in terms of accuracy for both four- and two-class classifications and AUROC for two-class classification (p<0.001). Conclusions| A novel deep learning model, including a multimodal deep learning model and an airway-highlighting preprocessing algorithm from CT images obtained for other purposes, can provide significantly precise outcomes for OSA diagnosis

# Summary. An optional shortened abstract.
summary: ___SCI(E); IF=24.70, 3.80% (Q1)___ <br> _American Journal of Respiratory and Critical Care Medicine (AJRCCM, Early Accept)_

tags: ['AI', 'medical', 'Obstructive Sleep Apnea', 'Classification', 'CT', 'Multi-modal', 'Q1']

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
url_project: 'https://osa-ct.or.kr'
# url_slides: ''
url_source: 'https://doi.org/10.1164/rccm.202304-0767OC'
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
