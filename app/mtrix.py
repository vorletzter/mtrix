import pymumble_py3
import time
from pymumble_py3.callbacks import PYMUMBLE_CLBK_TEXTMESSAGERECEIVED as chat
from pymumble_py3.callbacks import PYMUMBLE_CLBK_USERCREATED as userJoined
from pymumble_py3.callbacks import PYMUMBLE_CLBK_USERREMOVED as userLeft
from matrix_client.client import MatrixClient
from matrix_client.api import MatrixRequestError

mumble_server = "mumble.luki.org"
mumble_user = "pythonBot"
mumble_pwd = ""

matrix_server = "https://synod.im"
matrix_user = "" # needed
matrix_pwd = "" # needed
matrix_room = "#mumbleMonitor:synod.im"

mumble = pymumble_py3.Mumble(mumble_server, mumble_user, password=mumble_pwd)
client = MatrixClient(matrix_server)
token = client.login(username=matrix_user, password=matrix_pwd)

try:
    room = client.join_room(matrix_room)
except MatrixRequestError as e:
    print(e)

def mumble_user_joined(user):
    channel = mumble.channels[user["channel_id"]].get_property("name")
    print(user["name"] + " has joined mumble in channel '" + mumble.channels[user["channel_id"]].get_property("name") + "'")
    room.send_text(user["name"] + " has joined mumble in channel '" + mumble.channels[user["channel_id"]].get_property("name") + "'")

def mumble_user_left(user, unused):
    print(user["name"] + " has left mumble")
    room.send_text(user["name"] + " has left mumble")

def mumble_user_chat(message):
    print(message)
    #room.send_text(message)


mumble.callbacks.set_callback(userJoined, mumble_user_joined)
mumble.callbacks.set_callback(userLeft, mumble_user_left)
mumble.callbacks.set_callback(chat, mumble_user_chat)
mumble.start()

while 1:
    time.sleep(1)
