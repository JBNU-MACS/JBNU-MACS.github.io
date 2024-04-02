---
title: 'CSS-Net: Classification and Substitution for Segmentation of Rotator Cuff Tear'

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here
# and it will be replaced with their full name and linked to their profile.
authors:
  - 이경수
  - 류하민
  - 이문환
  - 김준영
  - 황재윤

# Author notes (optional)
author_notes:
  - ''
  - ''
  - ''
  - ''
  - 'Corresponding author'
# {{equal}}

# date format: '2013-07-01T00:00:00Z'
date: '2022-12-08'
doi: 'https://doi.org/10.1007/978-3-031-26351-4_7'

# Schedule page publish date (NOT publication's date).
publishDate: '2022-12-08'

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ['paper-conference']

# Publication name and optional abbreviated publication name.
publication: Asian Conference on Computer Vision
publication_short: Asian Conference on Computer Vision (ACCV)  [__Top AI & CV Conference__]

abstract: Magnetic resonance imaging (MRI) has been popularly used to diagnose orthopedic injuries because it offers high spatial resolution in a non-invasive manner. Since the rotator cuff tear (RCT) is a tear of the supraspinatus tendon (ST), a precise comprehension of both is required to diagnose the tear. However, previous deep learning studies have been insufficient in comprehending the correlations between the ST and RCT effectively and accurately. Therefore, in this paper, we propose a new method, substitution learning, wherein an MRI image is used to improve RCT diagnosis based on the knowledge transfer. The substitution learning mainly aims at segmenting RCT from MRI images by using the transferred knowledge while learning the correlations between RCT and ST. In substitution learning, the knowledge of correlations between RCT and ST is acquired by substituting the segmentation target (RCT) with the other target (ST), which has similar properties. To this end, we designed a novel deep learning model based on multi-task learning, which incorporates the newly developed substitution learning, with three parallel pipelines- (1) segmentation of RCT and ST regions, (2) classification of the existence of RCT, and (3) substitution of the ruptured ST regions, which are RCTs, with the recovered ST regions. We validated our developed model through experiments using 889 multi-categorical MRI images. The results exhibit that the proposed deep learning model outperforms other segmentation models to diagnose RCT with 68

# Summary. An optional shortened abstract.
summary: ___ACCV 2022 (Top AI & CV Conference)___ <br> _Asian Conference on Computer Vision2022_

tags: ['AI', 'medical', 'segmentation', 'mathematics']

# Display this page in the Featured widget?
featured: true

# Custom links (uncomment lines below)
# links:
# - name: Custom Link
#   url: http://example.org

# url_pdf: '{{url_pdf}}'
url_code: 'https://github.com/kyungsu-lee-ksl/ACCV2022-Substitution-Learning'
# url_dataset: '{{url_dataset}}'
# url_poster: '{{url_poster}}'
# url_project: ''
# url_slides: ''
url_source: 'https://doi.org/10.1007/978-3-031-26351-4_7'
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
