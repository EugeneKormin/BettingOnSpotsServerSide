from flask import Flask
from flask import request
import os

print(f"current_path: {os.getcwd()}")
from API.API import API


app = Flask(__name__)


@app.route('/api/v1.0/predict', methods=['GET'])
def predict():
    return API(request).predict


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
