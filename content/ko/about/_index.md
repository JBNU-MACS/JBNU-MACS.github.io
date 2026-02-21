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
        content: 진단 지원 및 의료 데이터 기반 지능형 모델 연구
        align: left
        background:
          image:
            filename: medical.jpg
            filters:
              brightness: 0.34
          position: center
      - title: Multimodal Intelligence
        content: Vision & Language 기반의 멀티모달 AI 연구
        align: left
        background:
          image:
            filename: Ai.jpg
            filters:
              brightness: 0.34
          position: center
      - title: Applied AI Engineering
        content: 연구를 실제 서비스와 시스템으로 연결하는 개발
        align: left
        background:
          image:
            filename: development.jpg
            filters:
              brightness: 0.34
          position: center
    design:
      slide_height: '360px'
      is_fullscreen: false
      loop: true
      interval: 4200
  
---
