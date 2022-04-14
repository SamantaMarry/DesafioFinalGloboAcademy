from flask import Flask
from flask_restful import Api
from flask_cors import CORS, cross_origin


class Server:
    def __init__(
        self,
    ):
        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.cors = CORS(self.app)

    def run(
        self,
    ):
        self.app.run(debug=True, host="0.0.0.0", port=5000)


server = Server()
