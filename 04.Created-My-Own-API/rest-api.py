from flask import Flask

from bs4 import BeautifulSoup
import requests


def get_currency(in_currency, out_currency):
    url = f'https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1'
    content = requests.get(url).text
    soup = BeautifulSoup(content, 'html.parser')
    rate =soup.find("span", class_="ccOutputRslt").get_text()

    return rate

app = Flask(__name__)


@app.route('/')
def home():
    return '<h1>Currency Rate API</h1> <p> Example URL: /api/vi/usd-eur</p>'

@app.route('api/v1/<in_cur>-<out_cur>')
def api(in_cur, out_cur):
    rate = get_currency(in_cur, out_cur)


app.run(host='0.0.0.0')