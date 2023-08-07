import falcon.asgi, socketio

from src.middlewares.auth import Auth
from src.middlewares.pool import Pool
from src.socket.server import socket

from src.controllers import  users

app = falcon.asgi.App(middleware=[Pool(), Auth()])

users = users.UsersResource()

app.add_route('/users', users)
app.add_route('/users/{id}', users, suffix='user')

asgi = socketio.ASGIApp(socket, app)
