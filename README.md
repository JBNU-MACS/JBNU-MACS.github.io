# MACS Lab · 전북대학교

전북대학교 **Medical AI & Computational Science Laboratory (MACS Lab)** 홈페이지 저장소입니다. 의료영상, 멀티모달 학습, 계산과학을 중심으로 연구실의 연구 성과와 구성원, 학술 활동을 소개합니다.

- **홈페이지:** [jbnu.macs.or.kr](https://jbnu.macs.or.kr/)
- **언어:** [한국어](https://jbnu.macs.or.kr/ko/) · [English](https://jbnu.macs.or.kr/en/)
- **소속:** 전북대학교 컴퓨터인공지능학부
- **지도교수:** 이경수 (Kyungsu Lee)
- **문의:** [ksl@jbnu.ac.kr](mailto:ksl@jbnu.ac.kr)

## 사이트 구성

| 메뉴 | 내용 |
| --- | --- |
| 소개 | 연구실 소개, 연구 참여 및 대학원 진학 안내 |
| 구성원 | 교수, 연구원, 학생 및 졸업생 소개 |
| 연구 | 연구 분야와 논문, 연구 성과 |
| 소식 | 연구실 소식, 공지사항, 학술 활동 |
| 연락처 | 연구 참여·협업 문의 및 위치 안내 |

## 콘텐츠 관리

한국어 콘텐츠는 `content/ko/`, 영어 콘텐츠는 `content/en/`에서 관리합니다. 같은 내용을 두 언어로 게시할 때는 양쪽의 본문과 메타데이터를 함께 갱신합니다.

| 수정할 내용 | 경로 (`content/<언어>/` 기준) |
| --- | --- |
| 메인 페이지 구성 | `_index.md` |
| 연구실 소개 / 참여 안내 / 연락처 | `about/`, `join/`, `contact/` |
| 구성원 프로필 / 구성원 페이지 | `authors/`, `people/` |
| 연구 분야 / 논문 | `field/`, `publication/` |
| 연구실 소식 / 공지사항 / 학술 활동 | `post/`, `notification/`, `event/` |

새 글이나 논문은 같은 유형의 기존 폴더를 복사한 뒤 `index.md`의 제목, 날짜, 저자, 본문과 첨부 이미지를 수정합니다. 구성원 프로필은 `authors/<이름>/_index.md`에서 관리합니다. 복사한 항목의 기존 메타데이터와 링크가 남지 않았는지 확인하고, 로컬 미리보기에서 목록과 상세 페이지를 모두 확인해 주세요.

연구 참여를 마친 구성원은 `user_groups: ["Former Members"]`로 지정하고, `role`에는 `전 학부연구생` 등 이전 역할을 적습니다. 구성원 페이지의 ‘이전 구성원’에는 기존 `Alumni`도 함께 표시하며, 참여 기간과 종료 사유는 표시하지 않습니다. 한글·영문 프로필을 함께 수정합니다.

논문에는 `research_fields: ["ai", "medical-ai"]`처럼 관련 분야를 지정합니다. 분야 ID와 분류 기준은 [논문 연구 분야 안내](docs/publication-research-fields.md)를 참고하세요. 한글·영문 분류를 함께 수정한 뒤 `python3 scripts/check_research_fields.py`로 확인합니다. 이 분류는 연구 분야의 관련 논문과 논문 목록의 분야·연도·유형 필터에 공통으로 적용됩니다.

논문 목록에서는 Kyungsu Lee가 제1저자(공동 제1저자 포함) 또는 교신저자인 논문의 카드 배경만 흰색에 가까운 옅은 색으로 강조합니다. 첫 번째 저자는 `authors` 순서로, 공동 제1저자와 교신저자는 같은 위치의 `author_notes`에 있는 `Equal contribution`, `Corresponding author`로 판별합니다. 두 역할이면 하나의 메모에 함께 기록할 수 있습니다. 이 목록 강조에는 수동 `highlight` 값을 사용하지 않으며, 저자 정보는 한글·영문에 동일하게 반영합니다.

페이지 일부는 사용자 정의 템플릿으로 구성되어 있습니다. Markdown에 `{{< academic_home >}}` 같은 호출이 있으면 해당 화면의 구성과 문구는 `layouts/shortcodes/` 및 `layouts/partials/`도 확인합니다.

## 주요 디렉터리

| 경로 | 용도 |
| --- | --- |
| `content/ko/`, `content/en/` | 언어별 페이지와 콘텐츠 |
| `assets/media/` | 공용 이미지와 아이콘 |
| `assets/scss/`, `assets/js/` | 스타일과 화면 동작 |
| `layouts/` | 사용자 정의 페이지 템플릿, shortcode, partial |
| `static/` | 경로를 유지한 채 제공하는 정적 파일 |
| `config/_default/` | 사이트 기본 정보, 언어, 메뉴, 테마 설정 |
| `.github/workflows/publish.yaml` | GitHub Pages 빌드·배포 설정 |
| `public/` | 빌드 출력 위치 — 콘텐츠 수정은 원본 파일에서 진행 |

메뉴는 `menus.ko.yaml`과 `menus.en.yaml`, 사이트 주소와 기본 언어는 `hugo.yaml`, 언어별 콘텐츠 경로는 `languages.yaml`에서 설정합니다. 모두 `config/_default/` 안에 있습니다.

## 로컬 실행

Hugo **Extended 0.123.7**과 Go가 필요합니다. Hugo 버전은 현재 GitHub Actions 배포 설정과 동일하게 맞춥니다. 로컬 실행은 Go 1.21.5에서 확인했습니다.

저장소 루트에서 실행합니다. 첫 실행 시 테마 모듈을 다운로드하므로 인터넷 연결이 필요합니다.

```sh
hugo server --bind 127.0.0.1 --baseURL http://localhost:1313/ --renderToMemory
```

[한국어 미리보기](http://localhost:1313/ko/) 또는 [영어 미리보기](http://localhost:1313/en/)를 엽니다. 파일을 저장하면 자동으로 다시 빌드되며, 종료는 `Ctrl+C`입니다. 초안까지 확인하려면 실행 명령에 `--buildDrafts`를 추가합니다.

## 배포

`main` 브랜치에 push하면 GitHub Actions가 사이트를 빌드하고 GitHub Pages에 배포합니다. [배포 워크플로](https://github.com/JBNU-MACS/JBNU-MACS.github.io/actions/workflows/publish.yaml)에서 진행 상태를 확인하거나 수동 실행할 수 있습니다.

## 기반 및 라이선스

[Hugo](https://gohugo.io/)와 [HugoBlox Research Group 테마](https://github.com/wowchemy/starter-hugo-research-group)를 기반으로 연구실에 맞게 구성했습니다. 원본 테마의 MIT 라이선스와 저작권 고지는 [LICENSE.md](LICENSE.md)에 보존되어 있습니다.
