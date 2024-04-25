import requests

def get_weather(city, units='metric', api_key='0051bfbc99fb4c3a9ce9bf684b8edd48'): 
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units={units}'
    r = requests.get(url)
    content = r.json()
    with open('data.txt', 'a') as file:
        for dicty in content['list']:
            file.write(f"{dicty['dt_txt']}, {dicty['main']['temp']},{dicty['weather'][0]['description']}")
        # return content

print(get_weather(city='washington'))
