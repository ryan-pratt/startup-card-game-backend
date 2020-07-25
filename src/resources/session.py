from flask import request, jsonify, session
from flask_restful import Resource
from flask_socketio import join_room

class Start(Resource):
    def __init__(self, **kwargs):
        self.socketio = kwargs['socketio']
        self.redis_client = kwargs['redis_client']
    

    def post(self):
        code = request.json['code']
        
        self.redis_client.incr(code + ':playercount')

        session['gameCode'] = code
        session['playerId'] = 'host'
        return ("Started session " + code, 201)
    
    
    def put(self):
        code = request.json['code']

        player_id = self.redis_client.get(code + ':playercount')
        self.redis_client.incr(code + ':playercount')

        self.socketio.emit('player-join', {'playerCount': player_id}, room=code)

        session['gameCode'] = code
        session['playerId'] = player_id
        return (player_id, 200)
