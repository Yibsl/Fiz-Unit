import sqlite3 as sq
import random
import time
import Utils.Read_Write

while False:
    #Noch adden
    Zpos=get(pos_magnetencoder)
    direction=getdirection()

start=time.time()
print(start)
while time.time()-start<20:
#for i in range(0, 200):
    #print(i)
    Zoom=Utils.Read_Write.Zoom()
    Zoom.update_values(random.randint(0,100),"up")
    #print(Zoom.get("Pos"))
    time.sleep(0.1)
    
Zoom.close()

