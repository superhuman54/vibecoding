# 🤖 VibeCoding - AI 챗봇 프로젝트

> FastAPI 백엔드 + Streamlit 프론트엔드 + LangGraph Agent를 활용한 AI 챗봇 플랫폼

[![GitHub Actions](https://github.com/superhuman54/vibecoding/workflows/🧪%20테스트%20실행/badge.svg)](https://github.com/superhuman54/vibecoding/actions)
[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)](https://streamlit.io/)

## 🌟 주요 기능

- **🎯 AI 검색 챗봇**: Gemini-2.5-flash 모델과 DuckDuckGo 검색 통합
- **⚡ 실시간 응답**: FastAPI 기반 고성능 백엔드
- **🎨 직관적 UI**: Streamlit으로 구현된 사용자 친화적 인터페이스
- **🔧 자동화**: GitHub Actions를 통한 CI/CD 및 프로젝트 관리
- **🧪 TDD 지원**: 체계적인 테스트 주도 개발 환경

## 🏗️ 아키텍처

```
vibecoding/
├── backend/                    # FastAPI 백엔드
│   ├── app/
│   │   ├── main.py            # FastAPI 애플리케이션
│   │   ├── agent.py           # LangGraph Agent
│   │   ├── config.py          # 설정 관리
│   │   ├── models/            # 데이터 모델
│   │   └── routers/           # API 라우터
│   └── tests/                 # 백엔드 테스트
├── frontend/                   # Streamlit 프론트엔드
│   └── app.py                 # 메인 인터페이스
├── .github/workflows/          # GitHub Actions
└── docs/                      # 프로젝트 문서
```

## 🚀 빠른 시작

### 1. 저장소 클론

```bash
git clone https://github.com/superhuman54/vibecoding.git
cd vibecoding
```

### 2. 백엔드 설정

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. 환경 변수 설정

```bash
cp env.example .env
# .env 파일에서 API 키 설정
```

### 4. 백엔드 실행

```bash
python run.py
```

### 5. 프론트엔드 실행

```bash
cd frontend
pip install -r requirements.txt
streamlit run app.py
```

## 🔧 환경 변수

백엔드 `.env` 파일에 다음 변수들을 설정해야 합니다:

```env
GOOGLE_API_KEY=your_gemini_api_key_here
LANGSMITH_API_KEY=your_langsmith_api_key_here  # 선택사항
```

## 🧪 테스트

### 백엔드 테스트

```bash
cd backend
pytest tests/ -v --cov=app
```

### 코드 품질 검사

```bash
# 코드 포맷팅
black .
isort .

# 코드 품질 검사
flake8 .
mypy .

# 보안 검사
bandit -r .
safety check
```

## 🤖 GitHub Actions 자동화

프로젝트에는 다음과 같은 자동화 기능이 포함되어 있습니다:

### 📋 자동 테스트 및 품질 관리
- **테스트 실행**: push/PR 시 자동 테스트
- **코드 리뷰**: 자동 코드 품질 검사 및 보안 스캔
- **커버리지**: 테스트 커버리지 리포트

### 🏷️ 스마트 라벨링
- **타입**: `type/feature`, `type/bugfix`, `type/documentation`
- **우선순위**: `priority/critical`, `priority/high`, `priority/medium`, `priority/low`
- **영역**: `area/backend`, `area/frontend`, `area/agent`
- **크기**: `size/XS`, `size/S`, `size/M`, `size/L`, `size/XL`

### 👥 자동 할당
- 파일 경로 기반 담당자 할당
- 키워드 기반 전문가 할당
- 긴급 이슈 특별 처리

## 📝 기여 가이드

### 이슈 작성

이슈를 작성할 때 다음 형식을 사용해주세요:

```
제목: [타입] 간단한 설명
타입: bug, feature, enhancement, question, documentation

내용:
- 문제 설명 또는 요구사항
- 재현 단계 (버그의 경우)
- 예상 결과 vs 실제 결과
```

### PR 작성

PR을 작성할 때 다음 형식을 사용해주세요:

```
제목: [타입] 간단한 설명
타입: feat, fix, docs, style, refactor, test, chore

내용:
- 변경 사항 요약
- 테스트 결과
- 관련 이슈 번호
```

### 개발 프로세스 (TDD)

1. **테스트 코드 작성**
2. **코딩**
3. **테스트 실행**
4. **테스트 에러 수정 반복**
5. **전체 테스트 진행**

## 🛠️ 기술 스택

### 백엔드
- **Python 3.11**
- **FastAPI**: 고성능 웹 프레임워크
- **LangGraph**: AI Agent 구현
- **Gemini-2.5-flash**: LLM 모델

### 프론트엔드
- **Streamlit**: 빠른 웹 앱 개발

### AI/Agent
- **LangGraph**: React Agent 구현
- **DuckDuckGo Search**: 웹 검색 도구
- **LangSmith**: 모니터링 (선택사항)

### 개발 도구
- **pytest**: 테스트 프레임워크
- **Black, isort**: 코드 포맷팅
- **Flake8, MyPy**: 코드 품질 검사
- **Bandit, Safety**: 보안 검사

## 🔗 관련 링크

- [프로젝트 구조 문서](./.cursor/rules/project-structure.mdc)
- [GitHub 관리 규칙](./.cursor/rules/github-management.mdc)
- [기술 스택 상세](./.cursor/rules/tech-stack.mdc)
- [시스템 아키텍처](./.cursor/rules/system-architecture.mdc)

## 📄 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다.

## 🤝 기여자

- **[superhuman54](https://github.com/superhuman54)** - 프로젝트 메인테이너

---

**질문이나 제안사항이 있으시면 [이슈](https://github.com/superhuman54/vibecoding/issues)를 생성해 주세요!** 🚀 