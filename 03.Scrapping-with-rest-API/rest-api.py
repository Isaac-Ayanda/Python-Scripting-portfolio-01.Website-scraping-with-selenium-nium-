import requests

r = requests.get('https://newsapi.org/v2/everything?qInTitle=united%20states&from=2024-3-9&to=2024-3-27&sortBy=popularity&language=en&apiKey=890603a55bfa47048e4490069ebee18c')
content = r.json()
print(content)
print(type(content))
