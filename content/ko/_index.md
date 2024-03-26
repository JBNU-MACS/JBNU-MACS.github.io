---
# Leave the homepage title empty to use the site title
title:
date: 2024-03-25
type: landing

sections:

  - block: features
    content:
      title: <span style="font-size:70%">Medical AI & Computational Science (Macs) Lab </span>
      text: <br><span style="font-size:125%">전북대학교 의료 AI 및 계산 과학 연구실 홈페이지에 오신 것을 환영합니다.</span>

  - block: slider
    content:
      slides:

      - title: <span style="font-size:70%">Recruit</span>
        content: <span style="font-size:70%">Interested in MacsLAB?</span>
        align: center
        background:
          image:
            filename: recruitment.jpg
            filters:
              brightness: 0.1
          position: center
          color: '#000'
        link:
          icon: user
          icon_pack: fas
          text: <span style="font-size:60%">Join Us</span>
          url: contact

      - title: <span style="font-size:70%">AI</span>
        content: <span style="font-size:70%">의료/항공우주/컨텐츠 등 특성화 분야에 적용 가능한 AI 기술 개발<span style="font-size:70%">
        align: center
        background:
          image:
            filename: Ai.jpg
            filters:
              brightness: 0.3
          position: center
          color: '#000'

      - title: <span style="font-size:70%">Mathematics</span>
        content: <span style="font-size:70%">AI와 관련된 기반 이론 연구</span>
        align: center
        background:
          image:
            filename: mathematics.jpg
            filters:
              brightness: 0.5
          position: center
          color: '#000'

      - title: <span style="font-size:70%">Development</span>
        content: <span style="font-size:70%">기반 기술을 활용한 Full-Stack 어플리케이션 개발</span>
        align: center
        background:
          image:
            filename: development.jpg
            filters:
              brightness: 0.7
          position: center
          color: '#000'

    design:
      # Slide height is automatic unless you force a specific height (e.g. '400px')
      slide_height: '350px'
      slide_width: '100px'
      is_fullscreen: false
      # Automatically transition through slides?
      loop: true
      # Duration of transition between slides (in ms)
      interval: 3000


  - block: features
    id: features
    content:
      title: <span style="font-size:75%">Lab's Interests</span>
      text: 저희 연구실에서는 다음과 같은 연구/개발 분야에 관심을 쏟고 있습니다.<br><br><br><br>
      items:
        - name: 인공지능(AI)
          icon: magnifying-glass
          description: Automatic sitemaps, RSS feeds, and rich metadata take the pain out of SEO and syndication.<br><br>
        - name: 의료수학(Medical Math)
          icon: bolt
          description: Super fast page load with Tailwind CSS and super fast site building with Hugo.<br><br>
        - name: 멀티모달(Multi-modality)
          icon: medical
          icon_pack:
          description: One-click deployment to GitHub Pages. Have your new website live within 5 minutes!<br><br>
        - name: 컨텐츠 (Contents)
          icon: code-bracket
          description: Edit and design your site just using rich text (Markdown) and configurable YAML parameters.<br><br>
        - name: 개발 (Development)
          icon: star
          description: Rated 5-stars by the community.<br><br>
        - name: 솔루션 (Solution)
          icon: rectangle-group
          description: Build your pages with blocks - no coding required!<br><br>


  - block: collection
    content:
      title: Notifications & News
      subtitle:
      text:
      count: 2
      filters:
        author: ''
        category: ''
        exclude_featured: false
        publication_type: ''
        tag: ''
      offset: 0
      order: desc
      page_type: post
    design:
      view: compact
      columns: '2'

  - block: collection
    content:
      title: Latest Publications
      subtitle:
      text:
      count: 4
      filters:
        author: ''
        category: ''
        exclude_featured: false
        publication_type: ''
        tag: ''
      offset: 0
      order: desc
      page_type: publication
    design:
      view: citation
      columns: '2'
    advanced:
      css_style: "text-align: center;"

  - block: markdown
    content:
      title:
      subtitle:
      text: |
        {{% cta cta_link="./people/" cta_text="Meet the team →" %}} {{% cta cta_link="./contact/" cta_text="Join team →" %}}
    design:
      columns: '1'
---