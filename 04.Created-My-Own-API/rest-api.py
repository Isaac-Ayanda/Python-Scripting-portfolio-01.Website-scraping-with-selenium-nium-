from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return '<h1>Currency Rate API</h1> <p> Example URL: /api/vi/usd-eur</p>'

@app.route('api/v1/<in_cur>-<out_cur>')
def api(in_cur, out_cur):


app.run(host='0.0.0.0')