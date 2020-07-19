from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from resources import test

app = Flask(__name__)
app.secret_key = "hewwo" # TODO

# SESSION_COOKIE_DOMAIN = "http://localhost:3000"
CORS(app, supports_credentials=True, resources={r"/*": {"origins": "http://localhost:3000"}})
api = Api(app)

api.add_resource(test.HelloWorld, '/test')

if __name__ == '__main__':
    app.run(debug=True)