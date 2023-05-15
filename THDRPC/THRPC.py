from pypresence import Presence 
import pypresence
import time
import pystray
import PIL.Image
import psutil
import requests
import sys
import asyncio
from websockets import server
from websockets.sync.client import connect

start = int(time.time())
client_id = ''
oauth2token = ''

RPC = Presence(client_id)  
RPC.connect() 

def getinfo():
    c = pypresence.Client(client_id)
    c.start()

    auth = c.authorize(client_id, ['rpc'])
    code_grant = auth.code

    c.authenticate(oauth2token)
    
image = PIL.Image.open("THDRPC/logo.png")

def on_clicked(icon, item):
    icon.stop()
    print("quit")

icon = pystray.Icon("Neural", image, menu=pystray.Menu(
    pystray.MenuItem("exit", on_clicked)
))

def TH19():
    RPC.update(
    large_image="th19",
    state="Unfinished Dream of All Living Ghost",
    details="Touhou 19",
    large_text="TH19",
    start=start
)

def clientID():
    with connect("ws://127.0.0.1:6463/?v=VERSION&client_id=CLIENT_ID&encoding=ENCODING") as websocket:
        cliid = websocket.recv()

while True:  
    getinfo()
    clientID()
    icon.run()
    for proc in psutil.process_iter():
        match proc.name().lower():
            case "th19.exe":
                break

            case _:
                RPC.clear()

    time.sleep(15)