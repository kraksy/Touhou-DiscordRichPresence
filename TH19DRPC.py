from pypresence import Presence 
import time
import psutil

start = int(time.time())
client_id = "1106637916203135048"
RPC = Presence(client_id)  
RPC.connect() 

def TH19():
    RPC.update(
    large_image="th19",
    state="Unfinished Dream of All Living Ghost",
    details="Touhou 19",
    large_text="TH19",
    start=start
    )


while True:  
    
    for proc in psutil.process_iter():
        match proc.name().lower():
            case "th19.exe":
                break

            case _:
                RPC.clear()

    if TH19:


    time.sleep(15)