import requests

def get_news(country language='en', 
             api_key='aa27ff3681d34f0b88cfabe10e30dcac'): url = f'https://newsapi.org/v2/everything?qInTitle={topic}&from={from_date}&to={to_date}8&sortBy=popularity&language={language}&apiKey={api_key}'

r = requests.get(url)
content = r.json()

print(content)
