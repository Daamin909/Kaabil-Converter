import requests
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

def convert_currency(amount, from_currency, to_currency):
    url = f"https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_ZuGAAxXLvgIDdbeAWacrOONoWbvAKbtEh0JhSDZU&currencies={from_currency}%2C{to_currency}%2CUSD"
    response = requests.get(url)
    data = response.json()
    print(data)
    base_rate = data['data']['USD']/data['data'][from_currency]
    converted_amount = base_rate * amount * data['data'][to_currency]
    return converted_amount

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')
    # return f'{amount}{from_currency} = {convert_currency(float(amount), from_currency.upper(), to_currency.upper())} {to_currency}'
@app.route('/convert', methods=['POST'])
def convert():
    amount = request.form.get('amount')
    from_currency = request.form.get('fromCurrency')
    to_currency = request.form.get('toCurrency')
    return render_template('index.html',output=f'{convert_currency(float(amount), from_currency.upper(), to_currency.upper())} {to_currency}')

if __name__ == '__main__':
    app.run(host='127.0.0.1',port='8000',debug=True)