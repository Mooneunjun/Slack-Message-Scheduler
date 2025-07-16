

# 📨 Slack Message Auto-Sender Template

이 저장소는 특정 요일에 자동으로 Slack 메시지를 전송하는 Python 기반 스크립트를 제공합니다.  
간단한 설정으로 팀의 **데일리 알림**, **업무 지시**, **스탠드업 템플릿** 등을 자동화할 수 있습니다.

---

## ✅ 기능 요약

- 특정 요일에만 자동 전송 (예: 화~금)
- Slack 메시지 포맷 사용자 정의 가능
- `.env`로 민감 정보 관리
- 크론탭, GitHub Actions, Supabase 등 다양한 예약 실행 방식 지원

---

## 🔧 Slack App 구성 방법

1. **Slack App 생성**
   - https://api.slack.com/apps 접속 → **"Create New App"**
   - 이름 및 워크스페이스 선택 후 생성

2. **OAuth Token 생성**
   - `OAuth & Permissions` 메뉴로 이동
   - `Bot Token Scopes`에 아래 권한 추가:
     - `chat:write` – 메시지 전송 권한
   - **Install to Workspace** 클릭
   - 생성된 **Bot User OAuth Token (`xoxb-...`) 복사**

3. **슬랙 채널 초대**
   - Slack에서 봇을 메시지를 보낼 채널에 초대합니다:
     ```
     /invite @your_bot_name
     ```

4. **채널 ID 확인**
   - https://api.slack.com/methods/conversations.list → 테스트 콘솔에서 채널 목록 조회
   - 혹은 채널 URL에서 ID 확인 (`C012ABCDEF` 형식)

---

## 🛠️ 사용법

### 1. 설치

```bash
git clone https://github.com/yourname/slack-message-scheduler.git
cd slack-message-scheduler
pip install -r requirements.txt
```

### 2. 환경 변수 설정

`.env.example` 파일을 복사하고 Slack 정보를 입력하세요:

```bash
cp .env.example .env
```

`.env` 예시:

```env
SLACK_TOKEN=xoxb-your-slack-bot-token
CHANNEL_ID=C12345678
```

### 3. 메시지 항목 구성

`main.py`의 `message_items` 리스트를 원하는 내용으로 수정하세요.

---

## 🕒 자동 실행 방법 (크론/스케줄러)

다음 중 하나를 사용해 스크립트를 자동 실행할 수 있습니다.

### ✅ 1. Linux Crontab (서버 내 자동 실행)

```bash
crontab -e
```

예: 매주 화\~금 오전 9시 실행

```
0 9 * * 2-5 /usr/bin/python3 /your/path/main.py
```

### ✅ 2. GitHub Actions (무료 CI 인프라 활용)

```yaml
# .github/workflows/scheduler.yml
name: Scheduled Slack Message

on:
  schedule:
    - cron: '0 0 * * 2-5'  # UTC 기준 → 한국시간 오전 9시
  workflow_dispatch:

jobs:
  post-slack-message:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run script
        env:
          SLACK_TOKEN: ${{ secrets.SLACK_TOKEN }}
          CHANNEL_ID: ${{ secrets.CHANNEL_ID }}
        run: python main.py
```

> ✅ GitHub에 `Settings > Secrets` 에 `SLACK_TOKEN`, `CHANNEL_ID` 등록 필요

### ✅ 3. Supabase Scheduled Edge Functions (서버리스 + 정확한 실행)

* Supabase의 Edge Function + Cron을 사용하여 정확한 요일/시간에 실행 가능
* JavaScript 기반이며, Python 호출도 가능 (HTTP API 형태로 실행 가능)
* 참고: [Supabase Scheduled Functions Docs](https://supabase.com/docs/guides/functions/schedule-functions)

### ✅ 4. Cloud Scheduler (Google Cloud)

* Python script를 GCP Cloud Functions 또는 Cloud Run에 배포하고
* Cloud Scheduler로 요일/시간 예약 호출
* 신뢰성과 확장성 필요할 경우 적합

---

## 📂 파일 구성

```
slack-message-scheduler/
├── main.py               # 메시지 전송 스크립트
├── .env.example          # 환경 변수 예시
├── requirements.txt      # 의존성 목록
└── README.md             # 설명서
```

---

## 📄 라이선스

MIT License
자유롭게 수정/배포 가능하나, Slack API 규정 및 보안 정책을 준수해주세요.



