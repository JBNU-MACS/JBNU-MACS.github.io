---
title: 'Imbalanced Loss-integrated Deep-learning-based Ultrasound Image Analysis For Diagnosis Of Rotator-cuff Tear'

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here
# and it will be replaced with their full name and linked to their profile.
authors:
  - 이경수
  - 김준영
  - MoonHwan Lee
  - 최창혁
  - 
  - 황재윤

# Author notes (optional)
author_notes:
  - 'Equal contribution'
  - 'Equal contribution'
  - ''
  - 'Corresponding author'
  - ''
  - 'Corresponding author'
# {{equal}}

# date format: '2013-07-01T00:00:00Z'
date: '2021-03-22'
doi: 'https://doi.org/10.3390/s21062214'

# Schedule page publish date (NOT publication's date).
publishDate: '2021-03-22'

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ['article-journal']

# Publication name and optional abbreviated publication name.
publication: Sensors
publication_short: Sensors (Sensors)  [__SCI(E); IF=3.85, 28.91% (Q2)__]

abstract: __SCI(E); IF=3.85, 28.91% (Q2)__ <br> Sensors (Sensors, 2021, Vol. 21, Issue 6, Sensors (Sensors, 2021, Vol. 21, Issue 6) <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br>A rotator cuff tear (RCT) is an injury in adults that causes difficulty in moving, weakness, and pain. Only limited diagnostic tools such as magnetic resonance imaging (MRI) and ultrasound Imaging (UI) systems can be utilized for an RCT diagnosis. Although UI offers comparable performance at a lower cost to other diagnostic instruments such as MRI, speckle noise can occur the degradation of the image resolution. Conventional vision-based algorithms exhibit inferior performance for the segmentation of diseased regions in UI. In order to achieve a better segmentation for diseased regions in UI, deep-learning-based diagnostic algorithms have been developed. However, it has not yet reached an acceptable level of performance for application in orthopedic surgeries. In this study, we developed a novel end-to-end fully convolutional neural network, denoted as Segmentation Model Adopting a pRe-trained Classification Architecture (SMART-CA), with a novel integrated on positive loss function (IPLF) to accurately diagnose the locations of RCT during an orthopedic examination using UI. Using the pre-trained network, SMART-CA can extract remarkably distinct features that cannot be extracted with a normal encoder. Therefore, it can improve the accuracy of segmentation. In addition, unlike other conventional loss functions, which are not suited for the optimization of deep learning models with an imbalanced dataset such as the RCT dataset, IPLF can efficiently optimize the SMART-CA. Experimental results have shown that SMART-CA offers an improved precision, recall, and dice coefficient of 0.604% (+38.4%), 0.942% (+14.0%) and 0.736% (+38.6%) respectively. The RCT segmentation from a normal ultrasound image offers the improved precision, recall, and dice coefficient of 0.337% (+22.5%), 0.860% (+15.8%) and 0.484% (+28.5%), respectively, in the RCT segmentation from an ultrasound image with severe speckle noise. The experimental results demonstrated the IPLF outperforms other conventional loss functions, and the proposed SMART-CA optimized with the IPLF showed better performance than other state-of-the-art networks for the RCT segmentation with high robustness to speckle noise.

# Summary. An optional shortened abstract.
# summary: A rotator cuff tear (RCT) is an injury in adults that causes difficulty in moving, weakness, and pain. Only limited diagnostic tools such as magnetic resonance imaging (MRI) and ultrasound Imaging (UI) systems can be utilized for an RCT diagnosis. Although UI offers comparable performance at a lower cost to other diagnostic instruments such as MRI, speckle noise can occur the degradation of the image resolution. Conventional vision-based algorithms exhibit inferior performance for the segmentation of diseased regions in UI. In order to achieve a better segmentation for diseased regions in UI, deep-learning-based diagnostic algorithms have been developed. However, it has not yet reached an acceptable level of performance for application in orthopedic surgeries. In this study, we developed a novel end-to-end fully convolutional neural network, denoted as Segmentation Model Adopting a pRe-trained Classification Architecture (SMART-CA), with a novel integrated on positive loss function (IPLF) to accurately diagnose the locations of RCT during an orthopedic examination using UI. Using the pre-trained network, SMART-CA can extract remarkably distinct features that cannot be extracted with a normal encoder. Therefore, it can improve the accuracy of segmentation. In addition, unlike other conventional loss functions, which are not suited for the optimization of deep learning models with an imbalanced dataset such as the RCT dataset, IPLF can efficiently optimize the SMART-CA. Experimental results have shown that SMART-CA offers an improved precision, recall, and dice coefficient of 0.604% (+38.4%), 0.942% (+14.0%) and 0.736% (+38.6%) respectively. The RCT segmentation from a normal ultrasound image offers the improved precision, recall, and dice coefficient of 0.337% (+22.5%), 0.860% (+15.8%) and 0.484% (+28.5%), respectively, in the RCT segmentation from an ultrasound image with severe speckle noise. The experimental results demonstrated the IPLF outperforms other conventional loss functions, and the proposed SMART-CA optimized with the IPLF showed better performance than other state-of-the-art networks for the RCT segmentation with high robustness to speckle noise.

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
url_source: 'https://doi.org/10.3390/s21062214'
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
