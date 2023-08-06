import falcon.asgi, socketio

from src.middlewares.auth import Auth
from src.middlewares.pool import Pool
from src.socket.server import socket

from errors.storage import StorageError

from src.controllers import  users

app = falcon.asgi.App(middleware=[Pool(), Auth()])

users = users.UsersResource()

app.add_route('/users', users)
app.add_route('/users/{id}', users, suffix='user')

app.add_error_handler(Exception, StorageError.handle)

asgi = socketio.ASGIApp(socket, app)
