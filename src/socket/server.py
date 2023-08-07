import socketio

socket = socketio.AsyncServer(async_mode='asgi', logger=True, cors_allowed_origins='*')
