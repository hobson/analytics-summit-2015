#!/home/laneh/.virtualenvs/analytics-summit-2015/bin/python
from gevent import monkey
monkey.patch_all()

import os

from paws import app, socketio, db, redis_db

from paws.models import User, Presentation, Choice
from flask.ext.script import Manager, Shell

manager = Manager(app)

def make_shell_context():
    return dict(app=app, redis_db=redis_db, db=db, User=User, 
                Presentation=Presentation, Choice=Choice)

manager.add_command("shell", Shell(make_context=make_shell_context))

@manager.command
def syncdb():
    db.create_all()

@manager.command
def runserver():
    socketio.run(app, "0.0.0.0", port=5001)

@manager.command
def clear_redis():
    from paws.config import REDIS_SERVER, REDIS_PORT, REDIS_DB
    if REDIS_PORT:
        import redis
        redis_cli = redis.StrictRedis(host=REDIS_SERVER, port=REDIS_PORT, db=REDIS_DB)
        redis_cli.delete('left')
        redis_cli.delete('right')
    else:
        print("Not using redis, using RAM db instead, so just restart `runserver` to clear the database.")

if __name__ == '__main__':
    manager.run()

