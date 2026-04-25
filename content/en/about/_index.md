---
# Leave the homepage title empty to use the site title
title:
date: 2024-03-25
type: landing

sections:
  - block: markdown
    content:
      title:
      subtitle:
      text: |
        {{< about_fancy >}}
    design:
      columns: '1'
  
  - block: slider
    content:
      id: about-fancy-slider
      slides:
      - title: MACS Lab
        content: Medical AI & Computational Science
        align: left
        background:
          image:
            filename: pic-jbnu.jpg
            filters:
              brightness: 0.28
          position: center
      - title: Medical AI
        content: Intelligent model research based on diagnostic support and medical data
        align: left
        background:
          image:
            filename: medical.jpg
            filters:
              brightness: 0.34
          position: center
      - title: Multimodal Intelligence
        content: Multimodal AI research based on Vision & Language
        align: left
        background:
          image:
            filename: Ai.jpg
            filters:
              brightness: 0.34
          position: center
      - title: Applied AI Engineering
        content: Development that connects research to real services and systems
        align: left
        background:
          image:
            filename: development.jpg
            filters:
              brightness: 0.34
          position: center
    design:
      # Slide height is automatic unless you force a specific height (e.g. '400px')
      slide_height: '360px'
      is_fullscreen: false
      loop: true
      interval: 4200

---

