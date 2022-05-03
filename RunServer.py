from flask import Flask
from flask import request
from socket import gethostname
from socket import gethostbyname

from API.API import API


app = Flask(__name__)


@app.route('/api/v1.0/predict', methods=['GET'])
def predict():
    return API(request).predict


if __name__ == '__main__':
    IP: str = gethostbyname(gethostname())
    app.run(host=IP, port=105, debug=True)
