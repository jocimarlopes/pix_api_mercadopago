from flask import Flask, jsonify, make_response, request
import payments
import helpers

app = Flask(__name__)

@app.route('/get_payment')
def get_payment():
    data = request.json
    print(data)
    try:
        if data['price'] and data['description']:
            res = payments.get_payment(data['price'], data['description'])
            return jsonify(res)
    except:
        return make_response('Bad Request', 400)

@app.route('/verify_payment')
def verify_payment():
    data = request.json
    print(data)
    try:
        if data['id']:
            res = payments.verify_payment(data['id'])
            return jsonify(res) 
    except:
        return make_response('Bad Request', 400)

if __name__ == '__main__':
    helpers.verify_credentials()
    app.run(debug=True)