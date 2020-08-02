from flask import request, jsonify, session
from flask_restful import Resource
from flask_socketio import emit

class Card(Resource):
    def __init__(self, **kwargs):
        self.socketio = kwargs['socketio']
        self.redis_client = kwargs['redis_client']

    def get(self):
        code = session['gameCode']
        card = self.redis_client.lpop(code + ':deck')
        return (card, 200)

    def put(self):
        code = session['gameCode']
        card = request.json['cardId']
        self.redis_client.lpush(code + ':discard', card)
        return ('', 200)