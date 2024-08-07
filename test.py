from flask import Flask, request, jsonify

app = Flask(__name__)
@app.route('/send', methods=['GET'])
def get_example():
    name = request.args.get('fromCurrency', 'amount', 'toCurrency') 
@app.route('/post', methods=['POST'])
def post_example():
    data = request.get_json()
    message = data.get('message', 'No message received')
    print(message)
    return jsonify({'received_message': message})

if __name__ == '__main__':
    app.run(debug=True)
