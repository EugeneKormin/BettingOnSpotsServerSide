from flask import Flask
from flask import request

from API.API import API
from Train.TrainModel import TrainModel


app = Flask(__name__)


@app.route('/api/v1.0/predict', methods=['GET'])
def predict():
    return API(request).predict


@app.route('/api/v1.0/train', methods=['GET'])
def train():
    TrainModel()
    return "model successfully trained"


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
