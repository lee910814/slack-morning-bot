from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import os
from dotenv import load_dotenv
from weather import get_weather
from news import get_news_summary
from datetime import datetime

load_dotenv()

class MorningBot:
    def __init__(self):
        self.client = WebClient(token=os.getenv("SLACK_BOT_TOKEN"))
        self.channel = os.getenv("SLACK_CHANNEL_ID")
        self.token = os.getenv("SLACK_BOT_TOKEN")
        self.channel = os.getenv("SLACK_CHANNEL_ID")
    
    def send_morning_alert(self):
        """아침 알림 전송"""
        
        print(f"[{datetime.now()}] 아침 알림 준비 중...")
        
        # 각 정보 수집
        weather = get_weather("Seoul")
        news = get_news_summary()
        
        # 할 일 목록 (나중에 DB나 파일에서 가져올 수 있음)
        todo_list = """
✅ **오늘의 할 일**
- 10:00 - 팀 미팅
- 14:00 - 프로젝트 리뷰
- 17:00 - 주간 보고서 작성
"""
        
        # 메시지 조합
        message = f"""
안녕하세요! 🌅
오늘도 좋은 하루 되세요!

{weather}

{news}

{todo_list}

---
_자동 생성된 메시지입니다 | {datetime.now().strftime('%Y-%m-%d %H:%M')}_
"""
        
        # Slack 전송
        try:
            response = self.client.chat_postMessage(
                channel=self.channel,
                text=message,
                mrkdwn=True
            )
            print(f"✅ 메시지 전송 성공! (ts: {response['ts']})")
            
        except SlackApiError as e:
            print(f"❌ 에러 발생: {e.response['error']}")
            
    
    def test_message(self):
        """테스트 메시지 (바로 전송)"""
        print("테스트 메시지 전송 중...")
        self.send_morning_alert()

if __name__ == "__main__":
    bot = MorningBot()
    bot.test_message()  # 일단 테스트
    bot.send_morning_alert()  # 한 번만 실행
    print("알림 전송 완료!")