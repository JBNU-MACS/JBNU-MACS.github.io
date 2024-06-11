---
title: People
date: 2022-10-24

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

  - block: people
    content:
      title: Researchers
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
      show_interests: false
      show_role: true
      show_social: false
      columns: 3
---