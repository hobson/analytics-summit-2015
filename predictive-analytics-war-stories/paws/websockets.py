from flask.ext.socketio import emit

from . import socketio


@socketio.on('connect', namespace='/paws')
def test_connect():
    pass

@socketio.on('disconnect', namespace='/paws')
def test_disconnect():
    pass

