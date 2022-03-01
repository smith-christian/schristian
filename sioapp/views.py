#####################################################################################################################################
###########################         CODE BY SMITH CHRISTIAN / christian.smith.stanley@gmail.com           ###########################
#####################################################################################################################################

from django.shortcuts import render

# Create your views here.
import json
import socketio
from bson import ObjectId

from  sioapp.sparser.sparser import SerialData
# from sioapp.models import SensorData

sio = socketio.Server(cors_allowed_origins="*")


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

@sio.event
def connect(sid, environ):
    print('[INFO] Connect to client', sid)

@sio.event
def my_message(sid, data):
    if data:
        SERIAL_DATA = SerialData(data)
        n = SERIAL_DATA.parse()
        
        sio.emit("my_message", JSONEncoder().encode(n))
        # nes = SensorData()
        # nes.val = JSONEncoder().encode(n)
        # nes.save()
    
# @sio.event
# def test_data(sid,data):
#     print(data)
#     sio.emit("test_data", data)

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

@sio.event
def hello_esi(request):
    return render(request, "sioapp/html/index.html", {"data": "display_data if display_data else None" })

def esi(request):
    return render(request, "sioapp/html/autoreload.html", {"data":"display_data"})