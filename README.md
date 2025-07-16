# Slack-Message-Scheduler

이 스크립트는 매일 특정 요일에 자동으로 Slack 메시지를 전송하는 템플릿입니다.

## 사용법

1. `.env.example` 파일을 복사해 `.env`로 만들고, `SLACK_TOKEN`, `CHANNEL_ID` 값을 설정하세요.
2. 원하는 메시지를 `message_items` 배열에 작성하세요.
3. 원하는 요일만 전송되도록 `SEND_DAYS`를 수정하세요.
4. 크론탭이나 Supabase Scheduled Edge Function 등으로 주기 실행하세요.

## 의존성 설치

```bash
pip install python-dotenv requests
