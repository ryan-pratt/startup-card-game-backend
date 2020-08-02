from flask import Flask
from flask_cors import CORS
from flask_redis import FlaskRedis
from flask_restful import Api
from flask_socketio import SocketIO, emit, join_room
from resources import session, start, turn, card, hand

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('secrets.Config')

CORS(app, supports_credentials=True, resources={r"/*": {"origins": "http://localhost:3000"}})
socketio = SocketIO(app, cors_allowed_origins="http://localhost:3000")

api = Api(app)
redis_client = FlaskRedis(app, decode_responses=True)


# TODO: flask DI?
api.add_resource(session.Session, '/session', resource_class_kwargs={ 'socketio': socketio, 'redis_client': redis_client })
api.add_resource(start.Start, '/start', resource_class_kwargs={ 'socketio': socketio, 'redis_client': redis_client })
api.add_resource(turn.Turn, '/turn', resource_class_kwargs={ 'socketio': socketio, 'redis_client': redis_client })
api.add_resource(card.Card, '/card', resource_class_kwargs={ 'socketio': socketio, 'redis_client': redis_client })
api.add_resource(hand.Hand, '/hand', resource_class_kwargs={ 'socketio': socketio, 'redis_client': redis_client })


@socketio.on('join')
def on_join(data):
    room = data['room']
    join_room(room)


if __name__ == '__main__':
    socketio.run(app)