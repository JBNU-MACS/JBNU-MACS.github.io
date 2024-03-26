---
# Leave the homepage title empty to use the site title
title:
date: 2024-03-25
type: landing

sections:

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
    design:
      # Slide height is automatic unless you force a specific height (e.g. '400px')
      slide_height: '350px'
      is_fullscreen: false
      # Automatically transition through slides?
      loop: true
      # Duration of transition between slides (in ms)
      interval: 3000

  - block: markdown
    content:
      title: Medical AI & Computational Science (MACS) Lab
      text: 전북대학교 의료 AI 및 계산 수학 연구실 홈페이지에 오신 것을 환영합니다. 
  
  - block: hero
    content:
      title: Build Your Landing Pages with Hugo Blox
      text: 🧱 EASY. FREE (OPEN SOURCE). NO-CODE  🧱
      primary_action:
        text: Get Started
        url: https://hugoblox.com/templates/
        icon: rocket-launch
      secondary_action:
        text: Read the docs
        url: https://docs.hugoblox.com
      announcement:
        text: "Announcing the release of version 1."
        link:
          text: "Read more"
          url: "/blog/"
    design:
      spacing:
        padding: [0, 0, 0, 0]
        margin: [0, 0, 0, 0]
      # For full-screen, add `min-h-screen` below
      css_class: "dark"
      background:
        color: "navy"
        image:
          # Add your image background to `assets/media/`.
          filename: coders.jpg
          filters:
            brightness: 0.5

  - block: resume-biography
    content:
      # The user's folder name in content/authors/
      username: admin
    design:
      spacing:
        padding: [0, 0, 0, 0]
      biography:
        style: 'text-align: justify; font-size: 0.8em;'
        
  - block: features
    id: features
    content:
      title: Lab's Interests
      text: 저희 연구실에서는 다음과 같은 연구/개발 분야에 관심을 갖고 있습니다.<br><br><br><br>
      items:
        - name: AI
          icon: magnifying-glass
          description: Automatic sitemaps, RSS feeds, and rich metadata take the pain out of SEO and syndication.
        - name: Fast
          icon: bolt
          description: Super fast page load with Tailwind CSS and super fast site building with Hugo.
        - name: Easy
          icon: medical.svg
          description: One-click deployment to GitHub Pages. Have your new website live within 5 minutes!
        - name: No-Code
          icon: code-bracket
          description: Edit and design your site just using rich text (Markdown) and configurable YAML parameters.
        - name: Highly Rated
          icon: star
          description: Rated 5-stars by the community.
        - name: Swappable Blocks
          icon: rectangle-group
          description: Build your pages with blocks - no coding required!

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
        {{% cta cta_link="./people/" cta_text="Meet the team →" %}}
    design:
      columns: '1'
---