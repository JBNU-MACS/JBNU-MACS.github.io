---
# Leave the homepage title empty to use the site title
title:
date: 2024-03-25
type: landing

sections:


  - block: slider
    content:
      slides:

      - title: MACS Lab
        content: 전북대학교 의료 AI 및 계산 과학 연구실 홈페이지에 오신 것을 환영합니다.
        align: left
        background:
          image:
            filename: pic-jbnu.jpg
            filters:
              brightness: 0.25
          position: center
          color: '#0b1220'
        link:
          icon: book-open
          icon_pack: fas
          text: See Research Field →
          text-color: '#fff'
          url: field

      - title: Join MACS
        content: Research + Engineering를 함께 성장시키고 싶다면 지금 지원하세요.
        align: left
        background:
          image:
            filename: recruitment.jpg
            filters:
              brightness: 0.3
          position: center
          color: '#0b1220'
        link:
          icon: user
          icon_pack: fas
          text: Join Us
          text-color: '#fff'
          url: contact

      - title: AI Research
        content: 의료·항공우주·컨텐츠 등 특성화 분야에 적용 가능한 AI 기술 개발
        align: left
        background:
          image:
            filename: Ai.jpg
            filters:
              brightness: 0.3
          position: center
          color: '#0b1220'


      - title: Development
        content: 기반 기술을 활용한 Full-Stack 어플리케이션 개발
        align: left
        background:
          image:
            filename: development.jpg
            filters:
              brightness: 0.3
          position: center
          color: '#0b1220'

      - title: Medical AI
        content: 의료AI를 통한 질병 진단 및 환경 개선
        align: left
        background:
          image:
            filename: medical.jpg
            filters:
              brightness: 0.3
          position: center
          color: '#0b1220'

      - title: Mathematics
        content: AI와 관련된 수학 및 최적화 이론 연구
        align: left
        background:
          image:
            filename: mathematics.jpg
            filters:
              brightness: 0.3
          position: center
          color: '#0b1220'


    design:
      # Slide height is automatic unless you force a specific height (e.g. '400px')
      slide_height: '500px'
      slide_width: '100px'
      is_fullscreen: false
      # Automatically transition through slides?
      loop: true
      # Duration of transition between slides (in ms)
      interval: 6200
    advanced:
      css_style: |
        .slick-prev, .slick-next, .carousel-control-next-icon, .carousel-control-prev-icon {
          display: none !important;
        }


  - block: markdown
    content:
      title:
      subtitle:
      text: |
        {{< fancy_feature_grid >}}
    design:
      columns: '1'

  - block: markdown
    content:
      title:
      subtitle:
      text: |
        {{< home_dual_feed >}}
    design:
      columns: '1'

  - block: markdown
    content:
      title:
      subtitle:
      text: |
        {{% cta cta_link="./contact/" cta_text="Join team →" %}}
    design:
      columns: '1'
---
