from flask import Flask
from flask import request

from API.API import API


app = Flask(__name__)


@app.route('/api/v1.0/predict_score', methods=['GET'])
def predict():
    return API(request=request).predicted_score


@app.route('/api/v1.0/calculate_advance', methods=['GET'])
def calculate_advance():
    return API(request=request).advance


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
