import requests
import anthropic
import os
from dotenv import load_dotenv

load_dotenv()

def get_news_summary():
    """네이버 뉴스 크롤링 후 AI 요약"""
    
    # 간단하게 RSS 사용 (크롤링보다 안정적)
    url = "https://news.google.com/rss?hl=ko&gl=KR&ceid=KR:ko"
    
    try:
        response = requests.get(url)
        
        # 간단한 파싱 (실제로는 feedparser 라이브러리 추천)
        # 여기서는 간단히 텍스트로 처리
        news_data = response.text[:3000]  # 처음 3000자만
        
        # Claude에게 요약 요청
        client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
        
        message = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=500,
            messages=[{
                "role": "user",
                "content": f"""다음 뉴스 데이터에서 주요 뉴스 3개를 골라서 각각 한 문장으로 요약해줘.
                
형식:
1. [카테고리] 요약 내용
2. [카테고리] 요약 내용
3. [카테고리] 요약 내용

데이터:
{news_data}"""
            }]
        )
        
        summary = message.content[0].text
        return f"📰 **오늘의 주요 뉴스**\n{summary}"
        
    except Exception as e:
        return f"뉴스를 가져올 수 없습니다: {str(e)}"