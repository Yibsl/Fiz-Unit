import sqlite3 as sq
import random
import time
import Utils.Read_Write

while False:
    #Noch adden
    Fpos=get(pos_magnetencoder)
    direction=getdirection()


def get_status():
    #connetct to Info Database
    return "Status"

start=time.time()
print(start)
while time.time()-start<20:
#for i in range(0, 200):
    #print(i)
    Focus=Utils.Read_Write.Focus()
    Focus.update_values(random.randint(0,100),"up")
    #print(Focus.get("Pos"))
    time.sleep(0.1)
    

Focus.close()

