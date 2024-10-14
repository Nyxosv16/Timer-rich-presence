from pypresence import Presence
import time
from datetime import datetime

client_id = 'CLIENT_BOT_ID'  
RPC = Presence(client_id)

print("Starting...")
RPC.connect()

try:
    while True:
        current_time = datetime.now().strftime("%H:%M:%S")
        
        
        RPC.update(state=f"Heure actuelle: {current_time}", large_image="IMAGE")
        
        
        print(f"Heure actuelle: {current_time}")
        
        
        time.sleep(1)

except KeyboardInterrupt:
    print("Exiting...")
finally:
    RPC.close()  
