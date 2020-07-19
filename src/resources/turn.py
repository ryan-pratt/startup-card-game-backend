from flask import request, jsonify, session
from flask_restful import Resource
from flask_socketio import emit

class Turn(Resource):
    def __init__(self, **kwargs):
        self.socketio = kwargs['socketio']

    def post(self):
        code = session['gameCode']
        playerId = session['playerId']
        self.socketio.emit('test', {'playerId': playerId}, room=code)
        return ("", 200)