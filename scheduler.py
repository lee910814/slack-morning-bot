import schedule
import time
from main import MorningBot

def job():
    """매일 실행될 작업"""
    print("스케줄 작업 시작...")
    bot = MorningBot()
    bot.send_morning_alert()

# 매일 오전 9시에 실행
schedule.every().day.at("09:00").do(job)

print("🤖 Morning Bot 시작!")
print("매일 오전 9시에 알림을 보냅니다.")
print("종료하려면 Ctrl+C를 누르세요.\n")

# 무한 루프
while True:
    schedule.run_pending()
    time.sleep(60)  # 1분마다 체크