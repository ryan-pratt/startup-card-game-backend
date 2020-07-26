from flask import request, jsonify, session
from flask_restful import Resource
from flask_socketio import join_room

class Start(Resource):
    def __init__(self, **kwargs):
        self.socketio = kwargs['socketio']
        self.redis_client = kwargs['redis_client']
    

    def post(self):
        code = session['gameCode']
        
        self.redis_client.delete(code + ':in-lobby')

        # TODO: set up deck, etc

        self.socketio.emit('start-game', {}, room=code)

        return ('', 200)
