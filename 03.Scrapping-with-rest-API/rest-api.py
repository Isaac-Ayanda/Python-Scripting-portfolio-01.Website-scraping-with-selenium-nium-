import requests

def get_news(country, api_key='890603a55bfa47048e4490069ebee18c'): url = f'https://newsapi.org/v2/top-headlines?qInTitle={topic}&from={from_date}&to={to_date}8&sortBy=popularity&language={language}&apiKey={api_key}'

r = requests.get(url)
content = r.json()
articles = content['articles']
results = []
for article in articles:



print(content)
