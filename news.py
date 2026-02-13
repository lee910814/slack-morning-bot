import feedparser
import re
from datetime import datetime
from collections import defaultdict

def get_news_summary():
    """AI 없이 똑똑한 뉴스 요약"""
    
    try:
        # 여러 RSS 소스 (더 풍부한 정보)
        feeds = [
            {
                'url': 'https://news.google.com/rss?hl=ko&gl=KR&ceid=KR:ko',
                'name': 'Google News'
            },
            {
                'url': 'https://www.hani.co.kr/rss/',
                'name': '한겨레'
            },
            {
                'url': 'http://www.hani.co.kr/rss/newsmaker/',
                'name': '한겨레 뉴스메이커'
            }
        ]
        
        all_news = []
        
        # 모든 피드에서 뉴스 수집
        for feed_info in feeds:
            try:
                feed = feedparser.parse(feed_info['url'])
                for entry in feed.entries[:10]:  # 각 소스에서 10개씩
                    all_news.append({
                        'title': clean_title(entry.title),
                        'link': entry.get('link', ''),
                        'source': feed_info['name'],
                        'summary': entry.get('summary', '')[:100]  # 요약이 있으면 사용
                    })
            except:
                continue
        
        # 중요도 기반 정렬 및 선택
        important_news = filter_and_rank_news(all_news)
        
        # 포맷팅
        result = format_news(important_news[:5])
        
        return result
        
    except Exception as e:
        return f"📰 뉴스를 가져올 수 없습니다: {str(e)}"


def clean_title(title):
    """제목 정리 (불필요한 기호 제거)"""
    # 출처 표시 제거 (예: "- 연합뉴스")
    title = re.sub(r'\s*-\s*[\w\s]+$', '', title)
    # 이상한 기호 제거
    title = re.sub(r'[【】\[\]]', '', title)
    return title.strip()


def filter_and_rank_news(news_list):
    """중요 뉴스 필터링 및 순위 매기기"""
    
    # 카테고리별 키워드 (중요도 점수)
    keywords = {
        '정치': {
            'keywords': ['대통령', '정부', '국회', '장관', '여당', '야당', '선거'],
            'weight': 3
        },
        '경제': {
            'keywords': ['주식', '코스피', '환율', 'GDP', '금리', '부동산', '삼성', 'SK', '현대'],
            'weight': 3
        },
        '사회': {
            'keywords': ['사고', '화재', '범죄', '재난', '날씨', '폭설', '폭우'],
            'weight': 2
        },
        '국제': {
            'keywords': ['미국', '중국', '일본', '북한', '전쟁', '트럼프', 'UN'],
            'weight': 2
        },
        '기술': {
            'keywords': ['AI', '인공지능', '챗GPT', '테슬라', '애플', '구글'],
            'weight': 1
        }
    }
    
    # 중복 제거 (유사한 제목)
    unique_news = remove_duplicates(news_list)
    
    # 점수 계산
    scored_news = []
    for news in unique_news:
        score = 0
        category = '기타'
        
        for cat, info in keywords.items():
            for keyword in info['keywords']:
                if keyword in news['title']:
                    score += info['weight']
                    category = cat
                    break
        
        news['score'] = score
        news['category'] = category
        scored_news.append(news)
    
    # 점수순 정렬
    scored_news.sort(key=lambda x: x['score'], reverse=True)
    
    return scored_news


def remove_duplicates(news_list):
    """유사한 뉴스 제거"""
    unique = []
    seen_keywords = set()
    
    for news in news_list:
        # 주요 단어 추출 (3글자 이상)
        words = [w for w in re.findall(r'\w+', news['title']) if len(w) >= 3]
        
        # 겹치는 단어가 2개 이상이면 중복으로 간주
        current_set = set(words[:5])  # 앞 5개 단어만 비교
        
        is_duplicate = False
        for seen in seen_keywords:
            if len(current_set & seen) >= 2:
                is_duplicate = True
                break
        
        if not is_duplicate:
            unique.append(news)
            seen_keywords.add(frozenset(current_set))
    
    return unique


def format_news(news_list):
    """뉴스 포맷팅"""
    
    result = "📰 **오늘의 주요 뉴스**\n"
    result += f"_{datetime.now().strftime('%Y년 %m월 %d일 %H시 기준')}_\n\n"
    
    for i, news in enumerate(news_list, 1):
        # 이모지 매핑
        emoji_map = {
            '정치': '🏛️',
            '경제': '💰',
            '사회': '🏙️',
            '국제': '🌍',
            '기술': '💻',
            '기타': '📌'
        }
        
        emoji = emoji_map.get(news['category'], '📌')
        
        result += f"{emoji} **{news['category']}**\n"
        result += f"{i}. {news['title']}\n"
        
        # 요약이 있으면 추가
        if news.get('summary') and len(news['summary']) > 20:
            result += f"   💬 {news['summary']}\n"
        
        result += f"   🔗 [기사 보기]({news['link']})\n\n"
    
    return result


# 백업: 초간단 버전
def get_simple_news():
    """가장 간단한 버전 (백업용)"""
    try:
        feed = feedparser.parse("https://news.google.com/rss?hl=ko&gl=KR&ceid=KR:ko")
        
        result = "📰 **오늘의 뉴스**\n\n"
        
        for i, entry in enumerate(feed.entries[:5], 1):
            result += f"{i}. {entry.title}\n"
            result += f"   🔗 {entry.link}\n\n"
        
        return result
    except:
        return "뉴스를 가져올 수 없습니다."