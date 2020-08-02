from flask import request, jsonify, session
from flask_restful import Resource
from flask_socketio import emit

class Hand(Resource):
    def __init__(self, **kwargs):
        self.socketio = kwargs['socketio']
        self.redis_client = kwargs['redis_client']

    def get(self):
        code = session['gameCode']
        playerId = session['playerId']
        hand = self.redis_client.lrange(code + ':' + playerId + ':hand', 0, -1)
        return (hand, 200)

    def post(self):
        code = session['gameCode']
        playerId = session['playerId']
        cards = request.json['cards']
        self.redis_client.delete(code + ':' + playerId + ':hand')
        for card in cards:
            self.redis_client.lpush(code + ':' + playerId + ':hand', card)
        return ('', 200)