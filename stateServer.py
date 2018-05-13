import socketio
import eventlet
import eventlet.wsgi
from flask import Flask, render_template

sio = socketio.Server()
app = Flask(__name__)

@sio.on('connect')
def connect(sid, environ):
    print("connect ", sid)

@sio.on('stateChanged')
def message(sid, data):
    print("message ", data)
    sio.emit('stateChanged', data)

@sio.on('disconnect')
def disconnect(sid):
    print('disconnect ', sid)

if __name__ == '__main__':
    # wrap Flask application with engineio's middleware
    app = socketio.Middleware(sio, app)

    # deploy as an eventlet WSGI server
    eventlet.wsgi.server(eventlet.listen(('', 8000)), app)