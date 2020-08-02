from flask import request, jsonify, session
from flask_restful import Resource
from flask_socketio import emit

class Turn(Resource):
    def __init__(self, **kwargs):
        self.socketio = kwargs['socketio']
        self.redis_client = kwargs['redis_client']

    def get(self):
        code = session['gameCode']
        turn_number = self.redis_client.get(code + ':turn')
        return (turn_number, 200)

    def post(self):
        code = session['gameCode']
        playerId = session['playerId']
        self.redis_client.incr(code + ':turn')
        return ("", 200)