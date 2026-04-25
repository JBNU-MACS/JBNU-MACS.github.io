---
title: 'PRIME: Ultra-Low-Rank Principal-Residual Model Merging'

# Authors
authors:
  - Seung-Ho Lee
  - Kyungsu Lee
  - Bazarvaani Zuchi
  - Jeongmin Ahn
  - Insuk Seo
  - Donghyeon Jeon
  - Inho Kang
  - Seung-Hoon Na

# Author notes (optional)
author_notes:
  - ''
  - 'Corresponding author'
  - ''
  - ''
  - ''
  - ''
  - ''
  - ''

# date format: '2013-07-01T00:00:00Z'
date: '2026-04-07'
doi: ''

# Schedule page publish date (NOT publication's date).
publishDate: '2026-04-07'

# Publication type.
publication_types:
  - conference-international

# Publication name and optional abbreviated publication name.
publication: ACL 2026 Findings
publication_short: Findings of ACL 2026

abstract: Model merging has emerged as an effective approach for integrating multiple task-specific fine-tuned models into a single unified model without requiring additional data-intensive training. A central challenge in model merging is to reduce task interference while preserving the task-specific capabilities of the original models. In this work, we propose PRIME, an ultra-low-rank principal-residual model merging framework that decomposes task vector merging into two complementary stages. First, ultra-low-rank principal task vector merging retains only a small fraction of singular vectors, effectively reducing task interference while preserving most of the task-specific performance. Second, orthogonal residual task vector merging incorporates the remaining components by projecting them onto the null space of the principal subspace, thereby avoiding interference while recovering additional task-relevant information. Extensive experiments on eight natural language processing tasks demonstrate that PRIME consistently outperforms existing model merging methods, achieving improvements of up to 1.18% on T5 and 1.9% on LLaMA-3.2-3B.

# Summary. An optional shortened abstract.
summary: '___ACL 2026 Findings___ <br> _Published: 2026.04.07 (Last Modified: 2026.04.18)_'

tags: ['AI', 'model merging', 'data-free merging', 'task vectors', 'NLP']

# Display this page in the Featured widget?
featured: true

url_code: ''
url_source: 'https://openreview.net/forum?id=g0cGQcokU5'
---
