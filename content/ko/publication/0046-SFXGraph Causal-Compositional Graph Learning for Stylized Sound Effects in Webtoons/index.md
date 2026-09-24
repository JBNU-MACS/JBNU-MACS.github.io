---
title: 'SFXGraph: Causal-Compositional Graph Learning for Stylized Sound Effects in Webtoons'

authors:
  - Sakang Hong
  - Haeyun Lee
  - Gunha Hong
  - Jinyoung Jung
  - Sanga Ahn
  - Kyungsu Lee

author_notes:
  - ''
  - ''
  - ''
  - ''
  - ''
  - 'Corresponding author'

date: '2026-09-22T00:00:00+09:00'
doi: ''
publishDate: '2026-09-22T00:00:00+09:00'

publication_types:
  - paper-csai

badges:
  - Top
  - BK/CS
highlight: true

publication: Asian Conference on Computer Vision 2026
publication_short: ACCV2026

abstract: >-
  Webtoons, a globally popular form of digital comics, rely on stylized sound effects (SFX) as essential visual cues for actions, emotions, and atmosphere. Since Webtoon SFX tightly entangle linguistic content, geometry, style, and scene context, conventional optical character recognition (OCR) systems designed for regular text often fail on these highly stylized effects. We propose SFXGraph, a causal-compositional graph parsing framework that models each SFX instance as a structured graph of linguistic units, geometric deformation, visual style, and contextual interaction factors, rather than decoding it as a flat text sequence. To learn this representation, we introduce counterfactual factor consistency, which separates scene-invariant content from SFX-induced factors and enforces the predicted graph to be sufficient for SFX removal, reconstruction, and controlled synthesis. We further construct a graph-supervised synthetic SFX generation pipeline that provides dense node, edge, style, and deformation supervision at scale. Experiments on public and custom Webtoon datasets demonstrate that SFXGraph consistently outperforms conventional OCR engines and vision--language baselines, while providing interpretable graph-level representations and stronger robustness to diverse artistic styles.

summary: ___ACCV2026___ <br> _Asian Conference on Computer Vision 2026_

tags: ['AI', 'computer vision', 'webtoon', 'sound effect recognition', 'causal-compositional graph parsing', 'counterfactual factor consistency']
featured: true

url_code: ''
url_project: ''
url_source: 'https://openreview.net/revisions?id=E0G0Yi1ASs'
---

### Framework Overview

[![SFXGraph framework showing SFX detection, graph parsing, text decoding, graph-conditioned rendering, and synthetic supervision.](featured.png)](featured.png)

*Figure 3 from the paper. SFXGraph represents stylized sound effects as structured graphs and uses graph-conditioned rendering and synthetic supervision to support recognition.*

### Recognition Results

[![Comparison of the original webtoon panel, four OCR baselines, and SFXGraph predictions.](recognition-results.png)](recognition-results.png)

*Figure 4 from the paper. From left to right: original panel, Naver Clova OCR, Keras OCR, Paddle OCR, Google OCR, and SFXGraph. Bounding boxes and transcriptions show detection and recognition outputs; "None" indicates a missed detection.*
