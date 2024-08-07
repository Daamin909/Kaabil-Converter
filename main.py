import requests
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


def get_data():
    url = "https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_ZuGAAxXLvgIDdbeAWacrOONoWbvAKbtEh0JhSDZU"
    response = requests.get(url)
    data = response.json()
    return data

def convert_currency(amount, from_currency, to_currency):
    data = get_data()
    base_rate = data['data']['USD']/data['data'][from_currency]
    converted_amount = base_rate * amount * data['data'][to_currency]
    return converted_amount

@app.route('/')
def home():
    return f'{convert_currency(1, "USD", "INR")}'

if __name__ == '__main__':
    app.run(host='127.0.0.1',port='8000',debug=True)
