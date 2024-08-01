from flask import Flask , request , jsonify
from flask_cors import CORS
import os
from scraper import amazon , snapdeal , flipkart

app = Flask(__name__)

CORS(app)

app.config['SECRET_KEY'] = os.urandom(64)


@app.route('/')
def home():
    return "Hello"


@app.route('/amazon' , methods=['POST'])
def amazon_data():
    body = request.get_json()
    query = body['data']
    app.logger.debug(query)

    data = amazon(query)
    app.logger.debug(data)
    return jsonify({'message': data}) , 200


@app.route('/snapdeal' , methods=['POST'])
def snapdeal_data():
    body = request.get_json()
    query = body['data']

    data = snapdeal(query)
    if 'message' in data.keys():
        return jsonify({'message': data['message']})
    else:
        return jsonify({'meassage': data}) , 200


@app.route('/flipkart' , methods=['POST'])
def flipkart_data():
    body = request.get_json()
    query = body['data']

    data = flipkart(query)
    app.logger.debug(data)
    return jsonify({'message': data})


if __name__ == '__main__':
    app.run(debug=True)
