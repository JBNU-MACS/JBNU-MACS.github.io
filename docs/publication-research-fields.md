# 논문 연구 분야 분류

연구 분야 버튼, 논문 목록 필터, 논문 상세의 분야 링크는 `research_fields`를 함께 사용합니다. 기존 `tags`는 키워드로 보존하며 분야 자동 판정에 사용하지 않습니다.

## 관리 방법

- 분야 ID·한영 표시명·페이지 경로·분류 범위: `data/research_fields.json`
- 연구 분야 페이지: front matter의 `research_field`에 단일 ID 지정
- 논문 페이지: `research_fields: ["ai", "medical-ai"]`처럼 하나 이상 지정. 한국어·영어 페이지에 같은 ID 목록을 유지합니다.
- 한 논문을 여러 분야에 분류할 수 있습니다. 분야별 건수의 합은 전체 논문 수와 다를 수 있습니다.
- 논문 목록 주소 예: `/ko/publication/?field=healthcare&year=2026&kind=journal#publications-index`. 분야·연도·유형 조건은 동시에 적용됩니다.
- 검증: `python3 scripts/check_research_fields.py`

## 분류 기준과 검토

2026-10-17 기준 저장소의 50개 논문 항목에 있는 제목과 초록을 검토했습니다. 학회 발표와 저널 확장판은 기존의 별도 항목을 유지했습니다. 분류는 연구 주제와의 관련성을 표시하며, 실제 제품 배포나 임상·로봇 자율제어 성과를 추가로 주장하지 않습니다.

- **인공지능 (`ai`)**: 학습 모델·컴퓨터 비전·표현 학습 등 AI 방법론. AI 모델을 사용하지 않는 기기·IoT 시스템 논문은 제외.
- **의료 AI (`medical-ai`)**: 의료영상·진단·생체신호·의료 기기와 분석 방법.
- **헬스케어 (`healthcare`)**: 모바일·웨어러블 건강 관리, 개인정보 보호, 개인화, 임상 업무와 사용자 중심 평가.
- **콘텐츠 (`contents`)**: 웹툰·스토리보드·시각 콘텐츠의 이해와 생성. 의료 영상 생성은 제외.
- **항공우주·원격탐사 (`aerospace`)**: 항공·위성 영상 기반 지리정보 분석. 실내 위치 추정과 지상 IoT 센싱은 제외.
- **의료수학·AI 수학 (`medical-mathematics`)**: 활성화·풀링·최적화·통계적 융합·베이지안 추정·잠재공간 등 수학적 방법이 핵심인 연구.
- **개발·시스템 (`development`)**: 모바일 기기, 진단 플랫폼, 실시간 애플리케이션, IoT·웹 대시보드 등 실제 시스템 구현.
- **계산과학 (`computational-science`)**: 수치적 형상·체적 추정, 물리 기반 시뮬레이션, 불확실성 정량화와 생체역학 모델링.
- **피지컬 AI (`physical-ai`)**: 탐촉자 이동 안내, 공간 위치 인식, 사람의 동작·생체신호와 로봇 보조 수술 작업의 이해. 자율제어 실적을 뜻하지 않음.

주의한 사례:
- 0023은 뇌의 연결 구조를 모방한 일반 신경망 방법론으로, 기존 `medical` 태그만을 근거로 의료 AI에 넣지 않았습니다.
- 0024의 실내 위치 추정은 피지컬 AI·개발에, 0030의 농업 IoT 시스템은 개발에 분류했습니다. 기존 원격탐사·AI 태그를 그대로 따르지 않았습니다.
- 0048의 단안 동작 분석과 0049의 EEG–시선 기반 로봇 보조 수술 평가를 피지컬 AI의 사람·작업 이해와 연결했습니다. 로봇 제어 연구로 분류한 것은 아닙니다.
- 0000·0001의 영상 기기/분석과 0030의 IoT 논문은 초록에서 AI 학습 모델이 확인되지 않아 일반 AI 분류에서 제외했습니다.

## 초기 분류표

이 표는 최초 분류 검토 기록입니다. 이후 변경 시에는 논문 front matter가 기준입니다.

| ID | 논문 | 연구 분야 ID |
| --- | --- | --- |
| 0000 | Smartphone-based Spectral Imaging Otoscope: System Development and Preliminary Study for Evaluation of Its Potential As a Mobile Diagnostic Tool | medical-ai, healthcare, development |
| 0001 | Wide-field 3D Ultrasound Imaging Platform with a Semi-Automatic 3D Segmentation Algorithm for Quantitative Analysis of Rotator Cuff Tears | medical-ai, development, computational-science |
| 0002 | Fully-automatic Deep Learning-based Analysis for Determination of the Invasiveness of Breast Cancer Cells in an Acoustic Trap | ai, medical-ai |
| 0003 | Domain Adaptive Transfer Attack-based Segmentation Networks for Building Extraction from Aerial Images | ai, aerospace |
| 0004 | Imbalanced Loss-Integrated Deep-Learning-based Ultrasound Image Analysis for Diagnosis of Rotator-Cuff Tear | ai, medical-ai, medical-mathematics |
| 0005 | Local Similarity Siamese Network for Urban Land Change Detection on Remote Sensing Images | ai, aerospace |
| 0006 | Federated Learning for Thyroid Ultrasound Image Analysis to Protect Personal Information: Validation Study in a Real Health Care Environment | ai, medical-ai, healthcare |
| 0007 | Boundary-oriented Binary Building Segmentation Model with Two Scheme Learning for Aerial Images | ai, aerospace |
| 0008 | Self-Mutating Network for Domain Adaptive Segmentation in Aerial Images | ai, aerospace |
| 0009 | Intelligent Smartphone-based Multimode Imaging Otoscope for the Mobile Diagnosis of Otitis Media | ai, medical-ai, healthcare, development |
| 0010 | Multi-task and Few-shot Learning-based Fully Automatic Deep Learning Platform for Mobile Diagnosis of Skin Diseases | ai, medical-ai, healthcare, development |
| 0011 | Speckle Reduction Via Deep Content-aware Image Prior for Precise Breast Tumor Segmentation in an Ultrasound Image | ai, medical-ai |
| 0012 | USG-Net: Deep Learning-based Ultrasound Scanning-Guide for an Orthopedic Sonographer | ai, medical-ai, healthcare, physical-ai |
| 0013 | Deep-Learning Model Associating Lateral Cervical Radiographic Features with Cormack--lehane Grade 3 Or 4 Glottic View | ai, medical-ai |
| 0014 | Stochastic Adaptive Activation Function | ai, medical-mathematics |
| 0015 | CSS-Net: Classification and Substitution for Segmentation of Rotator Cuff Tear | ai, medical-ai |
| 0016 | USIM Gate: Upsampling Module for Segmenting Precise Boundaries Concerning Entropy | ai, aerospace, medical-mathematics |
| 0017 | Self-supervised Domain Adaptive Segmentation of Breast Cancer Via Test-time Fine-Tuning | ai, medical-ai |
| 0018 | Fine-Tuning Network in Federated Learning for Personalized Skin Diagnosis | ai, medical-ai, healthcare, medical-mathematics |
| 0019 | Intelligent Bladder Volume Monitoring for Wearable Ultrasound Devices: Enhancing Accuracy through Deep Learning-based Coarse-to-Fine Shape Estimation | ai, medical-ai, healthcare, development, computational-science |
| 0020 | Fine-Grained Binary Object Segmentation in Remote Sensing Imagery via Path-Selective Test-Time Adaptation | ai, aerospace |
| 0021 | Predicting Obstructive Sleep Apnea Based on Computed Tomography Scan Using Deep Learning Models | ai, medical-ai, healthcare |
| 0022 | Machine Learning-Enhanced Skull-Universal Acoustic Hologram for Efficient Transcranial Ultrasound Neuromodulation Across Varied Rodent Skulls | ai, medical-ai, medical-mathematics, computational-science |
| 0023 | Connectome Mapping: Shape-Memory Network via Interpretation of Contextual Semantic Information | ai |
| 0024 | SoN: Selective Optimal Network for Smartphone-based Indoor Localization in Real-time | ai, development, physical-ai |
| 0025 | Interactive Few-shot Online Adaptation for User-Guided Segmentation in Aerial Images | ai, aerospace |
| 0026 | Real-time Self-supervised Ultrasound Image Enhancement Using Test-Time Adaptation for Sophisticated Rotator Cuff Tear Diagnosis | ai, medical-ai |
| 0027 | Human-Centered Personalization in Radiology AI: Evaluating Trust, Usability, and Cross-Hospital Robustness | ai, medical-ai, healthcare |
| 0028 | TCP: Context-Aware Pooling via Top-k% Activation Selection | ai, medical-mathematics |
| 0029 | Expert-level differentiation of incomplete Kawasaki disease and pneumonia from echocardiography via multiple large receptive attention mechanisms | ai, medical-ai |
| 0030 | Field Validated Hybrid ESP-NOW and Long Range IoT Monitoring System for Energy Autonomous Precision Agriculture | development |
| 0031 | Patient-Centric Statistical Multi-Modal Fusion for Medical Diagnosis: Integrating DICOM, Radiomics, and Patient Attributes | ai, medical-ai, healthcare, medical-mathematics |
| 0032 | Memory-Guided Personalization for Physician-Specific Diagnostic Inference | ai, medical-ai, healthcare |
| 0033 | Anatomy-Aware Distillation with Memory-Augmented SAM2 for Fracture Detection | ai, medical-ai |
| 0034 | SAM2-based Bayesian Prompt Adaptation for Cross-Modality Medical Segmentation | ai, medical-ai, medical-mathematics |
| 0035 | Statistical Latent Manifold-Guided Framework for Generative Super-Resolution | ai, medical-ai, medical-mathematics |
| 0036 | Statistical Multi-Modal Fusion for Patient-Centric Medical Diagnosis Using DICOM | ai, medical-ai, healthcare, medical-mathematics |
| 0037 | Statistical Latent Manifold-Guided Framework for Generative Super-Resolution | ai, medical-ai, medical-mathematics |
| 0038 | Anatomy-Aware Distillation with Memory-Augmented SAM2 for Fracture Detection | ai, medical-ai |
| 0039 | Bayesian Multiclass Segmentation for Remote Sensing: Integrating User Priors and Uncertainty | ai, aerospace, medical-mathematics, computational-science |
| 0040 | PRIME: Ultra-Low-Rank Principal-Residual Model Merging | ai, medical-mathematics |
| 0041 | Human-Intervention Segmentation via Federated Intent Embedding and Multi-Mask Recommendation | ai, medical-ai, healthcare |
| 0042 | Uncertainty-Aware Bayesian Prompt Adaptation of SAM2 for Few-Shot Cross-Modal Segmentation | ai, medical-ai, medical-mathematics |
| 0043 | Dynamic Sub-domain Modeling for Robust Medical Image Segmentation | ai, medical-ai |
| 0044 | Uncertainty-Aware Bayesian Prompt Adaptation for Robust Cross-Modality Medical Segmentation | ai, medical-ai, medical-mathematics |
| 0045 | Semantic Line Diffusion: Character-Consistent Line Art from Text-Annotated Storyboards | ai, contents |
| 0046 | SFXGraph: Causal-Compositional Graph Learning for Stylized Sound Effects in Webtoons | ai, contents |
| 0047 | Biomarker-Aware Mixture-of-Experts for Device-Invariant Personalized Skin Diagnosis | ai, medical-ai, healthcare |
| 0048 | Learning When to Correct: Selective Calibration for Monocular Kinematics | ai, healthcare, computational-science, physical-ai |
| 0049 | Modality-Aware Spectral Alignment for Personalized Federated EEG–Gaze Learning | ai, medical-ai, healthcare, physical-ai |
