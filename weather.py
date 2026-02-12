import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_weather(city="Seoul"):
    """날씨 정보 가져오기"""
    api_key = os.getenv("OPENWEATHER_API_KEY")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=kr"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        description = data['weather'][0]['description']
        humidity = data['main']['humidity']
        
        weather_text = f"""
🌤 **오늘의 날씨 ({city})**
- 기온: {temp}°C (체감 {feels_like}°C)
- 날씨: {description}
- 습도: {humidity}%
"""
        return weather_text
        
    except Exception as e:
        return f"날씨 정보를 가져올 수 없습니다: {str(e)}"