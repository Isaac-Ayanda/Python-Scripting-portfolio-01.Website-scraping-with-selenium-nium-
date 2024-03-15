from bs4 import BeautifulSoup

def get_currency(input_currency, output_currency):
    url = f'https://www.x-rates.com/calculator/?from={input_currency}&to={output_currency}&amount=1'
    print(url)

get_currency('INR', 'USD')
