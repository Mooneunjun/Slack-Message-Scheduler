import requests
import os
import time
from datetime import datetime, timedelta
from dotenv import load_dotenv

# ✅ .env 파일에서 환경 변수 로드
load_dotenv()

# ✅ 슬랙 설정
SLACK_TOKEN = os.getenv("SLACK_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID", "your-channel-id")

if not SLACK_TOKEN:
    raise ValueError("SLACK_TOKEN 환경 변수가 설정되지 않았습니다.")

# ✅ 시간대 설정 (한국 기준)
KST = timedelta(hours=9)
now = datetime.utcnow() + KST
weekday = now.weekday()  # 0=월요일, ..., 6=일요일

# ✅ 요일 제한 (원하는 요일만 전송)
SEND_DAYS = [1, 2, 3, 4]  # 화~금만 전송
if weekday not in SEND_DAYS:
    print("오늘은 메시지를 전송하지 않는 요일입니다.")
    exit()

# ✅ 날짜 포맷
formatted_date = now.strftime("%Y-%m-%d (%a)")

# ✅ 메시지 항목 예시 (원하는 메시지로 수정 가능)
message_items = [
    "할 일 1: TODO 항목 예시",
    "할 일 2: 데일리 스탠드업",
    "할 일 3: 리뷰 요청",
]

# ✅ 메시지 조합
header = f"*📅 {formatted_date} 자동 발송 메시지*"
body = "\n".join([f"{i+1}. {item}" for i, item in enumerate(message_items)])
full_message = f"{header}\n{'='*40}\n{body}"

# ✅ 슬랙 API 호출
def send_slack_message(text: str):
    url = "https://slack.com/api/chat.postMessage"
    headers = {
        "Authorization": f"Bearer {SLACK_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "channel": CHANNEL_ID,
        "text": text,
        "mrkdwn": True
    }
    res = requests.post(url, headers=headers, json=payload)
    result = res.json()
    if result.get("ok"):
        print("✅ 메시지 전송 성공")
    else:
        print(f"❌ 메시지 전송 실패: {result}")

send_slack_message(full_message)
