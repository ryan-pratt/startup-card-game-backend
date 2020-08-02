from flask import request, jsonify, session
from flask_restful import Resource
from flask_socketio import join_room
import random

class Start(Resource):
    def __init__(self, **kwargs):
        self.socketio = kwargs['socketio']
        self.redis_client = kwargs['redis_client']
    

    def post(self):
        code = session['gameCode']
        self.redis_client.delete(code + ':in-lobby')
        self.build_deck(code)
        # TODO: initial resource points, etc
        self.redis_client.set(code + ':turn', 0)
        self.socketio.emit('start-game', {}, room=code)
        return ('', 200)

    def build_deck(self, code):
        multiples = [ # how many of each card (with id of the index in this array) appear in the deck
            2,  # code monkey mike         (0)
            2,  # ambitious apprentice
            1,  # assertive cto
            2,  # copy paste dev
            2,  # downer dave
            2,  # database dev             (5)
            2,  # BI dev
            2,  # full stack ninja
            2,  # QA wizard
            2,  # senior backend dev
            2,  # junior backend dev       (10)
            2,  # research engineer
            2,  # lead dev
            2,  # intern
            1,  # shy frontend dev
            2,  # office manager           (15)
            2,  # rockstar recruiter
            2,  # undercover HR agent
            1,  # nice HR lady
            1,  # nice HR guy
            2,  # scrum master             (20)
            1,  # clean code
            1,  # design patterns
            1,  # defensive programming
            1,  # polymorphism
            1,  # TDD                      (25)
            1,  # unit tests
            1,  # SOLID
            1,  # version control
            1,  # domain knowledge
            1,  # dependency injection     (30)
            1,  # debugging
            1,  # CI
            2,  # outsourcing
            4,  # investor (might need to change -2 to 0 and add a rule) 
            1,  # head hunter              (35)
            1,  # coffee machine
            2,  # get away from it all
            1,  # crunch time
            1,  # technical debt
            2   # monster bug              (40)
        ]
        cards = []
        for i in range(len(multiples)):
            for j in range(multiples[i]):
                cards.append(i)
        random.shuffle(cards)
        self.redis_client.lpush(code + ':deck', *cards)
