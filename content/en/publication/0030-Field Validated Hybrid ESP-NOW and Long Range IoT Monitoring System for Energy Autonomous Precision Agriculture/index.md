---
title: 'Field Validated Hybrid ESP-NOW and Long Range IoT Monitoring System for Energy Autonomous Precision Agriculture'

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here
# and it will be replaced with their full name and linked to their profile.
authors:
  - Ali Abdelli
  - Wissem Boujnah
  - Younes Ben Salah
  - Khaled Issa
  - Hatem Garrab
  - Sarvar Hussain Nengroo
  - Mohsen Machhout
  - Kyungsu Lee

# Author notes (optional)
author_notes:
  - ''
  - ''
  - ''
  - ''
  - ''
  - ''
  - ''
  - ''
# {{equal}}

# date format: '2013-07-01T00:00:00Z'
date: '2025-12-08'
doi: 'https://doi.org/10.1109/ACCESS.2025.3641487'

# Schedule page publish date (NOT publication's date).
publishDate: '2025-12-08'

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ['article-journal']

# Publication name and optional abbreviated publication name.
publication: IEEE Access
publication_short: Access
journal_type: SCI(E)
impact_factor: '3.6'
jcr_rank: '35.9%'
jcr_percentile: 'Q2'

abstract: Agriculture in arid and semi-arid regions faces critical challenges of water scarcity, irregular rainfall, and the high cost of monitoring systems. Most existing Internet of Things (IoT) platforms for precision agriculture are expensive, energy-intensive, and rely on cellular or grid connectivity, which limits their adoption by smallholder farmers. To overcome these issues, this work presents a hybrid Espressif peer-to-peer protocol (ESP-NOW) / long range (LoRa) IoT monitoring system. The architecture combines ESP8266 sensor nodes, an ESP32 primary aggregator, and a Raspberry Pi 4 gateway, integrating ESP-NOW for local ultra-low-power communication and LoRa for long-range data transmission. In operation, the ESP8266 nodes periodically acquire environmental data and send it via ESP-NOW to the ESP32 primary, which aggregates the packets and forwards them through LoRa to the Raspberry Pi gateway for storage, visualization, and analysis. All sensor data are stored in a MySQL database and visualized in real time through a web dashboard. The sensing modules were calibrated under laboratory conditions using reference instruments to ensure accuracy, achieving correlation coefficients ( R2 ) between 0.95 and 0.97. Field deployment in a Tunisian wheat plot further confirmed stable performance, with less than 3% nighttime battery discharge and a packet delivery ratio above 95% up to 2 km. Costing under 600 EUR, the proposed system provides a validated, scalable, and affordable IoT solution for precision agriculture in resource-constrained environments.

# Summary. An optional shortened abstract.
summary: ___SCI(E); IF=3.60, 35.90% (Q2)___ <br> _IEEE Access (Vol. 13)_

tags: ['AI', 'Remote Sensing', 'Agriculture']

# Display this page in the Featured widget?
featured: false

# Custom links (uncomment lines below)
# links:
# - name: Custom Link
#   url: http://example.org

# url_pdf: '{{url_pdf}}'
# url_code: ''
# url_dataset: '{{url_dataset}}'
# url_poster: '{{url_poster}}'
url_project: ''
# url_slides: ''
url_source: 'https://ieeexplore.ieee.org/abstract/document/11282949'
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
