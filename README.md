# 🌅 Slack Morning Alert Bot

> 매일 아침 날씨, 뉴스, 할 일을 자동으로 알려주는 Slack 봇

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Slack](https://img.shields.io/badge/Slack-API-purple)
![GitHub Actions](https://img.shields.io/badge/GitHub-Actions-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

<p align="center">
  <img src="docs/demo.gif" alt="데모" width="600">
</p>

---

## 📋 목차

- [프로젝트 소개](#-프로젝트-소개)
- [주요 기능](#-주요-기능)
- [기술 스택](#-기술-스택)
- [시작하기](#-시작하기)
- [사용 방법](#-사용-방법)
- [프로젝트 구조](#-프로젝트-구조)
- [배포](#-배포)
- [트러블슈팅](#-트러블슈팅)
- [향후 계획](#-향후-계획)
- [기여하기](#-기여하기)
- [라이센스](#-라이센스)
- [연락처](#-연락처)

---

## 🎯 프로젝트 소개

매일 아침 출근 전, 날씨 확인하고 뉴스 검색하는 시간이 아깝다고 느꼈습니다.
**"이거 자동화하면 어떨까?"** 하는 생각에서 시작한 프로젝트입니다.

### 해결한 문제
- ❌ 매일 아침 여러 앱을 확인하는 번거로움
- ❌ 중요한 뉴스를 놓치는 일
- ❌ 팀원들과 정보 공유의 어려움

### 솔루션
- ✅ 매일 정해진 시간에 자동으로 정보 수집
- ✅ Slack 하나로 모든 정보 확인
- ✅ 팀 전체가 동일한 정보 공유

### 개발 기간 & 인원
- **기간**: 2026.02.13 (기능확장 예정)
- **인원**: 1명 (개인 프로젝트)
- **목적**: 포트폴리오 & 실제 사용

---

## ✨ 주요 기능

### 1. 🌤 실시간 날씨 정보
- OpenWeather API를 통한 현재 날씨
- 기온, 체감온도, 날씨 상태
- 습도 정보

### 2. 📰 주요 뉴스 요약
- Google News RSS 기반 뉴스 수집
- 카테고리별 자동 분류 (정치/경제/사회)
- 중복 뉴스 제거 알고리즘

### 3. ✅ 오늘의 할 일
- 일정 관리 및 리마인더
- 팀원 공통 일정 공유

### 4. ⏰ 완전 자동화
- GitHub Actions 기반 서버리스 실행
- 매일 정해진 시간 자동 발송
- 컴퓨터 꺼져도 작동

---

## 🛠 기술 스택

### Language & Framework
![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)

### APIs & Libraries
- **Slack SDK** `3.27.1` - Slack 메시지 전송
- **feedparser** `6.0.10` - RSS 뉴스 파싱
- **requests** `2.31.0` - HTTP 통신
- **python-dotenv** `1.0.1` - 환경변수 관리

### External APIs
- **Slack API** - 메시지 전송
- **OpenWeather API** - 날씨 정보
- **Google News RSS** - 뉴스 수집

### DevOps & CI/CD
- **GitHub Actions** - 서버리스 자동 실행
- **Git & GitHub** - 버전 관리

### Development Tools
- **VS Code** - 개발 환경
- **Git** - 버전 관리

---

## 🚀 시작하기

### 사전 요구사항
```bash
Python 3.12 이상
Git
Slack 워크스페이스 관리자 권한
```

### 설치 방법

#### 1. 저장소 클론
```bash
git clone https://github.com/lee910814/slack-morning-bot.git
cd slack-morning-bot
```

#### 2. 가상환경 생성 및 활성화
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

#### 3. 의존성 설치
```bash
pip install -r requirements.txt
```

#### 4. 환경변수 설정

`.env` 파일 생성:
```bash
cp .env.example .env
```

`.env` 파일 수정:
```env
SLACK_BOT_TOKEN=xoxb-your-slack-bot-token
SLACK_CHANNEL_ID=C04DEF456GH
OPENWEATHER_API_KEY=your-openweather-api-key
GOOGLE_API_KEY=your-google-gemini-key
```

---

## 🔑 API 키 발급 방법

### 1. Slack Bot Token

1. https://api.slack.com/apps 접속
2. "Create New App" 클릭
3. "From scratch" 선택
4. 앱 이름 & 워크스페이스 선택
5. **OAuth & Permissions** → Bot Token Scopes 추가:
   - `chat:write`
   - `channels:read`
6. "Install to Workspace" 클릭
7. **Bot User OAuth Token** 복사 (xoxb-로 시작)

### 2. Slack Channel ID

1. Slack 웹/앱에서 채널 클릭
2. 채널 이름 우클릭 → "링크 복사"
3. URL에서 마지막 부분 복사
```
   https://app.slack.com/client/T.../C04DEF456GH
                                    ^^^^^^^^^^^^
                                    이게 채널 ID
```

### 3. OpenWeather API Key

1. https://openweathermap.org/api 접속
2. 회원가입 (무료)
3. API Keys 메뉴에서 키 복사
4. ⚠️ 활성화까지 10분~2시간 소요

### 4. Google Gemini API Key (선택사항)

1. https://makersuite.google.com/app/apikey 접속
2. "Create API Key" 클릭
3. 키 복사
4. 무료 티어로 충분함

---

## 💻 사용 방법

### 로컬에서 테스트
```bash
# 단발성 실행
python main.py

# 스케줄러 실행 (로컬 테스트용)
python scheduler.py
```

### GitHub Actions로 자동화 (추천)

#### 1. GitHub Secrets 설정
```
GitHub 저장소 → Settings → Secrets and variables → Actions
→ New repository secret

다음 4개 추가:
- SLACK_BOT_TOKEN
- SLACK_CHANNEL_ID
- OPENWEATHER_API_KEY
- GOOGLE_API_KEY
```

#### 2. Push
```bash
git add .
git commit -m "feat: add GitHub Actions workflow"
git push origin main
```

#### 3. 자동 실행 확인
```
GitHub → Actions 탭
→ 매일 설정한 시간에 자동 실행
→ 수동 실행: "Run workflow" 버튼
```

---

## 📁 프로젝트 구조
```
slack-morning-bot/
├── .github/
│   └── workflows/
│       └── morning-alert.yml    # GitHub Actions 워크플로우
│
├── .env.example                  # 환경변수 템플릿
├── .gitignore                    # Git 제외 파일
│
├── main.py                       # 메인 실행 파일
├── weather.py                    # 날씨 API 모듈
├── news.py                       # 뉴스 수집/분류 모듈
├── scheduler.py                  # 로컬 스케줄러 (테스트용)
│
├── requirements.txt              # Python 패키지 목록
└── README.md                     # 프로젝트 문서
```

---

## 🏗 아키텍처
```
┌─────────────────────┐
│  GitHub Actions     │
│  (매일 16:30 실행)  │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   Python Script     │
│   (main.py)         │
└──────────┬──────────┘
           │
     ┌─────┴─────┐
     ▼           ▼
┌─────────┐  ┌─────────┐
│ Weather │  │  News   │
│   API   │  │   RSS   │
└────┬────┘  └────┬────┘
     │            │
     └─────┬──────┘
           ▼
    ┌─────────────┐
    │ Message     │
    │ Formatting  │
    └──────┬──────┘
           ▼
    ┌─────────────┐
    │  Slack API  │
    └──────┬──────┘
           ▼
    ┌─────────────┐
    │   #channel  │
    │  팀원들 수신 │
    └─────────────┘
```

---

## 🎨 주요 코드 설명

### 날씨 정보 수집 (weather.py)
```python
def get_weather(city="Seoul"):
    """OpenWeather API로 실시간 날씨 조회"""
    
    api_key = os.getenv("OPENWEATHER_API_KEY")
    url = f"http://api.openweathermap.org/data/2.5/weather"
    
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric",  # 섭씨
        "lang": "kr"
    }
    
    response = requests.get(url, params=params)
    data = response.json()
    
    return format_weather(data)
```

### 뉴스 분류 알고리즘 (news.py)
```python
def classify_news(title, keywords):
    """키워드 기반 뉴스 카테고리 분류"""
    
    for category, keyword_list in keywords.items():
        if any(keyword in title for keyword in keyword_list):
            return category
    
    return '기타'
```

### Slack 메시지 전송 (main.py)
```python
def send_morning_alert(self):
    """아침 알림 메시지 전송"""
    
    weather = get_weather("Seoul")
    news = get_news_summary()
    
    message = f"""
안녕하세요! 🌅
오늘도 좋은 하루 되세요!

{weather}

{news}

✅ 오늘의 할 일
- 10:00 - 팀 미팅
- 14:00 - 프로젝트 리뷰
"""
    
    self.client.chat_postMessage(
        channel=self.channel,
        text=message
    )
```

---

## 🐛 트러블슈팅

### 문제 1: `channel_not_found` 에러

**증상:**
```
❌ Error: channel_not_found
```

**원인:**
- 채널 ID가 잘못됨
- 봇이 채널에 초대되지 않음

**해결:**
```bash
1. 올바른 채널 ID 사용 (C로 시작)
2. Slack에서: /invite @봇이름
```

---

### 문제 2: OpenWeather API `401 Unauthorized`

**증상:**
```
401 Unauthorized
```

**원인:**
- API 키 활성화 대기 중 (10분~2시간)

**해결:**
```
키 발급 후 1-2시간 대기
```

---

### 문제 3: GitHub Actions 시간 안 맞음

**증상:**
- 설정한 시간에 실행 안 됨

**원인:**
- UTC/KST 시간대 차이

**해결:**
```yaml
# 한국 16:30 = UTC 7:30
cron: '30 7 * * *'

공식: UTC = 한국시간 - 9
```

---

## 📊 성능 & 비용

### 실행 시간
```
총 소요시간: 약 50-60초

단계별:
- 코드 체크아웃: 5초
- Python 설치: 10초
- 패키지 설치: 20초
- 스크립트 실행: 15-20초
```

### 비용
```
💰 총 비용: $0 (완전 무료!)

- Slack API: 무료
- OpenWeather API: 무료 (월 100만 요청)
- Google News RSS: 무료
- GitHub Actions: 무료 (월 2000분)
```

---

## 🔮 향후 계획

### Phase 1 (단기)
- [ ] 주식 시세 추가
- [ ] 환율 정보 추가
- [ ] 교통 정보 (출근길 소요 시간)
- [ ] 주말 제외 옵션

### Phase 2 (중기)
- [ ] 사용자별 맞춤 설정
- [ ] Slack Slash Commands 추가
- [ ] 웹 대시보드 구축
- [ ] 다중 채널 지원

### Phase 3 (장기)
- [ ] AI 기반 뉴스 요약
- [ ] 개인화 알고리즘
- [ ] SaaS 서비스화
- [ ] 유료 프리미엄 기능

---

## 🤝 기여하기

기여는 언제나 환영입니다! 

### 기여 방법

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### 코드 스타일

- PEP 8 준수
- 함수/변수명: snake_case
- 클래스명: PascalCase
- 주석: 한글 또는 영어

---

## 📄 라이센스

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 연락처

**이름** - 이OO

- 📧 Email: your.email@example.com
- 💼 LinkedIn: [linkedin.com/in/yourprofile](https://linkedin.com/in/yourprofile)
- 🐱 GitHub: [@lee910814](https://github.com/lee910814)
- 📝 Blog: [yourblog.com](https://yourblog.com)

**Project Link**: [https://github.com/lee910814/slack-morning-bot](https://github.com/lee910814/slack-morning-bot)

---

## 🙏 감사의 말

- [Slack API](https://api.slack.com/) - 훌륭한 API 문서
- [OpenWeather](https://openweathermap.org/) - 무료 날씨 API
- [GitHub Actions](https://github.com/features/actions) - 서버리스 실행 환경
- [Claude](https://claude.ai/) - 개발 과정 도움

---

<p align="center">
  Made with ❤️ by Lee910814
</p>

<p align="center">
  ⭐ 이 프로젝트가 도움이 되었다면 Star를 눌러주세요!
</p>
