from flask import Flask
from flask.ext.login import LoginManager
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.socketio import SocketIO

app = Flask(__name__, static_url_path='/static')
app.config.from_pyfile('config.py')

from config import REDIS_SERVER, REDIS_PORT, REDIS_DB

if REDIS_PORT:
    import redis
    redis_db = redis.StrictRedis(host=REDIS_SERVER, port=REDIS_PORT, db=REDIS_DB)
    VOTELOG = {}
else:
    redis_db = None
    VOTELOG = {
                'votes': dict([('paws' + str(i+1), 0) for i in range(6)]),
                'voters': {},
              }

socketio = SocketIO(app)
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.login_view = 'admin_sign_in'
login_manager.init_app(app)

from . import views
from . import websockets
