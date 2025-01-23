---
title: People
date: 2024-06-11

type: landing

sections:
  - block: people
    content:
      title: Professor
      # Choose which groups/teams of users to display.
      #   Edit `user_groups` in each user's profile to add them to one or more of these groups.
      user_groups:
          - Professor
      sort_by: Params.last_name
      sort_ascending: true
    design:
      show_interests: false
      show_role: true
      show_social: true
      show_organizations: true

  - block: people
    content:
      title: Student Researchers (Graduate)
      # Choose which groups/teams of users to display.
      #   Edit `user_groups` in each user's profile to add them to one or more of these groups.
      user_groups:
        - Ph.D. Student
        - M.S. Student
          # - 박사과정
          # - 석사과정
          # - 학부연구생
          # - Principal Investigators
          # - Researchers
          # - Grad Students
          # - Administration
          # - Visitors
          # - Alumni
      sort_by: Params.last_name
      sort_ascending: true
    design:
      show_interests: true
      show_role: true
      show_social: true
      show_organizations: false
      columns: 1

  - block: people
    content:
      title: Student Researchers (Undergraduate)
      # Choose which groups/teams of users to display.
      #   Edit `user_groups` in each user's profile to add them to one or more of these groups.
      user_groups:
        - Student
          # - 박사과정
          # - 석사과정
          # - 학부연구생
          # - Principal Investigators
          # - Researchers
          # - Grad Students
          # - Administration
          # - Visitors
          # - Alumni
      sort_by: Params.last_name
      sort_ascending: true
    design:
      show_interests: true
      show_role: true
      show_social: true
      show_organizations: false
      columns: 2

  - block: people   
    content:
      title: Alumni
      # Choose which groups/teams of users to display.
      #   Edit `user_groups` in each user's profile to add them to one or more of these groups.
      user_groups:
        - Alumni
          # - 박사과정
          # - 석사과정
          # - 학부연구생
          # - Principal Investigators
          # - Researchers
          # - Grad Students
          # - Administration
          # - Visitors
          # - Alumni
      sort_by: Params.last_name
      sort_ascending: true
    design:
      show_interests: false
      show_role: true
      show_social: true
      show_organizations: true
      columns: 2
---