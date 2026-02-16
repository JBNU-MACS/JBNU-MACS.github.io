---
title: 'TCP: Context-Aware Pooling via Top-k% Activation Selection'

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here
# and it will be replaced with their full name and linked to their profile.
authors:
  - Seo-Yeon Choi
  - Kyungsu Lee

# Author notes (optional)
author_notes:
  - ''
  - 'Corresponding author'
# {{equal}}

# date format: '2013-07-01T00:00:00Z'
date: '2026-01-31'
doi: ''

# Schedule page publish date (NOT publication's date).
publishDate: '2026-01-31'

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types:
  - paper-csai

# Publication name and optional abbreviated publication name.
publication: Annual Conference on Artificial Intelligence and Statistics
publication_short: AISTATS2026

abstract: Pooling is a fundamental operation in convolutional neural networks (CNN), leading to spatial reduction and hierarchical abstraction. However, conventional pooling methods such as max and average pooling operate locally and often fail to capture semantically meaningful features across the broader context of an image with under- or over-estimation. The inherent limitation hampers performance in vision tasks demanding both precise localization and global interpretation. To alleviate this, we introduce Top-K% Contextual Pooling (TCP), a novel pooling framework designed to retain the most informative activations based on the contextual importance. TCP consists of two variants (1) Sparse Contextual Pooling performs top-k selection within local kernel windows, and (2) Global Contextual Pooling identifies top-k% activations across the entire feature map. Given a kernel size and target output resolution, TCP automatically determines stride values and reconstructs the output through a deterministic process that preserves spatial coherence without additional learnable parameters. We evaluate TCP on a wide range of computer vision tasks including image classification, object detection, object tracking, semantic segmentation, and generation. Experimental results demonstrate consistent improvements in accuracy and robustness in vision tasks. Beyond performance gains, TCP provides a mechanism for interpreting model behavior by revealing how high-activation regions evolve across layers in the CNN pyramid. The hierarchical interpretation supports efficient representation while enabling layer-wise insight into the attention and decision patterns.




# Summary. An optional shortened abstract.
summary: ___AISTATS 2026 (Top AI & CV Conference)___ <br> _Annual Conference on Artificial Intelligence and Statistics 2026_

tags: ['AI', 'mathematics', 'Statistics']

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
url_source: ''
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
