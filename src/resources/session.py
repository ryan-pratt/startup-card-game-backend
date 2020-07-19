from flask import request, jsonify, session
from flask_restful import Resource

class Start(Resource):
    
    def post(self):
        code = request.json['code']
        session['gameCode'] = code
        session['playerId'] = 'host'
        # TODO: set redis keys
        return ("Started session " + code, 201)
    
    def put(self):
        code = request.json['code']
        # TODO: figure out player number from redis
        session['gameCode'] = code
        session['playerId'] = 1
        return (code, 200)
