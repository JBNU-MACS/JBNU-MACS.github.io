---
title: 'Semantic Line Diffusion: Character-Consistent Line Art from Text-Annotated Storyboards'

authors:
  - seoyeonchoi
  - kyungsulee

author_notes:
  - ''
  - 'Corresponding author'

date: '2026-06-18T00:00:00+09:00'
doi: ''
publishDate: '2026-06-18T00:00:00+09:00'

publication_types:
  - paper-csai

badges:
  - Top
  - BK/CS
highlight: true

publication: European Conference on Computer Vision 2026
publication_short: ECCV2026

abstract: >-
  Generating clean line art from conti, rough storyboard sketches used in webtoon production, remains a labor-intensive process requiring substantial artistic expertise. Conti sketches provide only coarse geometry and sparse semantic cues, making it difficult to recover detailed line art while preserving consistent character identity across sequential panels. Existing sketch-to-image or diffusion-based translation models process images independently and therefore struggle to maintain cross-panel identity coherence. We present PanelDiff, a diffusion transformer framework for conti-to-line-art generation that explicitly models cross-panel character consistency. PanelDiff integrates three components. A multi-reference character conditioning module encodes character labels and multiple line-art exemplars into compact identity tokens for robust identity guidance under ambiguous conti inputs. A memory-augmented representation bank accumulates character-aware features from previously generated panels, while a similarity interpreter dynamically retrieves relevant entries for the current panel. A panel-aware diffusion transformer then jointly attends to conti structure, textual descriptions, identity tokens, and retrieved memory features to produce coherent line-art sequences. To support this task, we construct a conti-line-art dataset with character identity annotations and sequential panel structures. Experiments show that PanelDiff improves line-art fidelity, identity preservation, and cross-panel consistency over strong baselines, and ablation studies verify the contribution of each component.

summary: ___ECCV2026___ <br> _European Conference on Computer Vision 2026_

tags: ['AI', 'computer vision', 'diffusion models', 'line art', 'storyboards', 'character consistency', 'webtoon']
featured: true

url_code: ''
url_project: ''
url_source: ''
---
