---
# Leave the homepage title empty to use the site title
title:
date: 2024-03-25
type: landing

sections:


  - block: slider
    content:
      slides:

      - title: <span style="font-size:70%">MacsLab</span>
        content: <span style="font-size:70%; line-height:1.15;">전북대학교 의료 AI 및 계산 과학 연구실 홈페이지에 오신 것을 환영합니다.</span>
        align: center
        background:
          image:
            filename: pic-jbnu.jpg
            filters:
              brightness: 0.3
          position: center
          color: '#000'
        link:
          icon: book-open
          icon_pack: fas
          text: <span style="font-size:70%">See Research Field →</span>
          text-color: '#000'
          url: field

      - title: <span style="font-size:70%">Recruit</span>
        content: <span style="font-size:70%">Interested in MacsLAB?</span>
        align: center
        background:
          image:
            filename: recruitment.jpg
            filters:
              brightness: 0.4
          position: center
          color: '#000'
        link:
          icon: user
          icon_pack: fas
          text: <span style="font-size:60%">Join Us</span>
          text-color: '#000'
          url: contact

      - title: <span style="font-size:70%">AI</span>
        content: <span style="font-size:70%; line-height:1.0;">의료/항공우주/컨텐츠 등 특성화 분야에 적용 가능한 AI 기술 개발<span style="font-size:70%">
        align: center
        background:
          image:
            filename: Ai.jpg
            filters:
              brightness: 0.4
          position: center
          color: '#000'


      - title: <span style="font-size:70%">Development</span>
        content: <span style="font-size:70%; line-height:1.0;">기반 기술을 활용한 Full-Stack 어플리케이션 개발</span>
        align: center
        background:
          image:
            filename: development.jpg
            filters:
              brightness: 0.4
          position: center
          color: '#000'

      - title: <span style="font-size:90%">Medical AI</span>
        content: <span style="font-size:70%">의료AI를 통한 질병 진단 및 환경 개선</span>
        align: center
        background:
          image:
            filename: medical.jpg
            filters:
              brightness: 0.4
          position: center
          color: '#000'

      - title: <span style="font-size:70%">Mathematics</span>
        content: <span style="font-size:70%">AI와 관련된 수학 및 최적화 이론 연구</span>
        align: center
        background:
          image:
            filename: mathematics.jpg
            filters:
              brightness: 0.4
          position: center
          color: '#000'


    design:
      # Slide height is automatic unless you force a specific height (e.g. '400px')
      slide_height: '330px'
      slide_width: '100px'
      is_fullscreen: false
      # Automatically transition through slides?
      loop: true
      # Duration of transition between slides (in ms)
      interval: 5500
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
