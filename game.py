from flask import jsonify
from google.appengine.api import users
from google.appengine.ext import db

class Game(db.Model):
    '''All the data we store for a game'''
    owner = db.StringProperty()
    joiner = db.StringProperty()

    # set to the current time, but only when entity is created
    start_time = db.DateTimeProperty(auto_now_add=True)
    # set to the current time, everytime model is stored
    last_time = db.DateTimeProperty(auto_now=True)

    # score information
    o_clicks = db.IntegerProperty()
    j_clicks = db.IntegerProperty()
    o_time = db.DateTimeProperty()
    j_time = db.DateTimeProperty()

    complete = db.BooleanProperty()

class GameUpdater():
    game = None

    def __init__(self, game):
        self.game = game

    def get_game_json(self):
        game_state = {
            'owner': self.game.owner,
            'joiner': self.game.joiner,
            'startTime': self.game.start_time,
            'lastTime': self.game.last_time,
            'oClicks': self.game.o_clicks,
            'jClicks': self.game.j_clicks,
            'oTime': self.game.o_time,
            'jTime': self.game.j_time,
            'complete': self.game.complete
        }
        return jsonify(game_state)

    def send_update_message(self):
        pass # for now

    def update(self, player, clicks, time):
        if player == self.game.owner:
            self.game.oClicks = clicks
            self.game.oTime = time
        elif plater == joiner:
            self.game.jClicks = clicks
            self.game.jTime = time
        else:
            print 'something went wrong - invalid player'

        self.game.put()
        self.send_update_message()

def create_game(player):
    game_id = None
    # initially o_time will be before start_time!
    game = Game(owner=player, o_clicks=0, o_time=datetime.utcnow())
    game.put()

    if game.is_saved():
        game_id = game.key().id()

    return game_id
