import socketio

socket = socketio.AsyncServer(async_mode='asgi', always_connect=True, logger=True, cors_allowed_origins='*')