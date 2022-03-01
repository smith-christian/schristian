# #####################################################################################################################################
# ###########################         CODE BY SMITH CHRISTIAN / christian.smith.stanley@gmail.com           ###########################
# #####################################################################################################################################

# import json

# import eventlet
# import socketio

# from sparser.sparser import SerialData

# sio = socketio.Server()
# # app = socketio.WSGIApp(sio)
# app = socketio.WSGIApp(sio, static_files={
#     '/': './Frontend/reactsio/public'
#     })


# @sio.event
# def connect(sid, environ):
#     print('[INFO] Connect to client', sid)

# @sio.event
# def my_message(sid, data):
#     if data:
#         SERIAL_DATA = SerialData(data)
#         n = SERIAL_DATA.parse()
#         sio.emit("my_message", json.dumps(str(n)))

#     # collection.insert_one(data)

# @sio.event
# def disconnect(sid):
#     print('disconnect ', sid)

# #ESI.local 192.168.2.95
# if __name__ == '__main__':
#     eventlet.wsgi.server(eventlet.listen(('', 5100)), app)
