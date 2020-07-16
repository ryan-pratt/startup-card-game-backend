from flask import Flask
from flask_restful import Api
from resources import test

app = Flask(__name__)
api = Api(app)

api.add_resource(test.HelloWorld, '/test')

if __name__ == '__main__':
    app.run(debug=True)