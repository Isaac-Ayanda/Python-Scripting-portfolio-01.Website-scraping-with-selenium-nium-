import requests

def get_weather(city, units='metrics', api_key='0051bfbc99fb4c3a9ce9bf684b8edd48'): 
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units={units}'
    r = requests.get(url)
    content = r.json()
    return content

print(get_news(country='us'))
