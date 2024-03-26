---
# Leave the homepage title empty to use the site title
title:
date: 2024-03-25
type: landing

sections:

  - block: features
    content:
      title: 
      text: <br><span style="font-size:125%">Macs에서는 의료, EMR, Vision, 항공, 국방 등 여러 분야에 AI 및 딥러닝을 활용한 연구를 수행하고 있으며, 의료 수학 및 AI 기반 연구도 함께 수행하고 있습니다. 뿐만 아니라, 풀스택 개발 및 AI를 활용한 어플리케이션 개발 등 Development & Deploy하는 실용적인 분야에도 집중하고 있습니다.</span>

  - block: slider
    content:
      slides:
      - title: AI
        content: 'Just opened last month!'
        align: center
        background:
          image:
            filename: welcome.jpg
            filters:
              brightness: 0.5
          position: center
          color: '#333'
      - title: Medical AI
        content: Take a look at what we're working on...
        align: center
        background:
          image:
            filename: coders.jpg
            filters:
              brightness: 0.7
          position: right
          color: '#666'
      - title: Development
        content: 'Share your knowledge with the group and explore exciting new topics together!'
        align: center
        background:
          image:
            filename: contact.jpg
            filters:
              brightness: 0.7
          position: center
          color: '#555'
      - title: Mathematics
        content: 'Just opened last month!'
        align: center
        background:
          image:
            filename: welcome.jpg
            filters:
              brightness: 0.5
          position: center
          color: '#333'
        link:
          icon: graduation-cap
          icon_pack: fas
          text: Join Us
          url: ../contact/
    design:
      # Slide height is automatic unless you force a specific height (e.g. '400px')
      slide_height: '350px'
      is_fullscreen: true
      # Automatically transition through slides?
      loop: true
      # Duration of transition between slides (in ms)
      interval: 3000

  # - block: hero
  #   content:
  #     title: |
  #       <span style="font-size:75%">Medical AI & Computational Science (MACS) Lab</span>
  #     image:
  #       filename: welcome.jpg
  #     text: |
  #       <br>
        
  #       <span style="font-size:75%">전북대학교 의료 AI 및 계산 수학 연구실 (MACS Lab) 홈페이지에 오신 것을 환영합니다. MACS에서는 의료, 항공, 국방 분야에 AI 및 딥러닝을 활용한 연구를 수행하고 있으며, 의료 수학 및 AI 기반 연구도 함께 수행하고 있습니다. 뿐만 아니라, 풀스택 개발 및 AI를 활용한 어플리케이션 개발 등 Development & Deploy하는 실용적인 분야에도 집중하고 있습니다.</span>
  
---