import sqlite3 as sq
import random
import time
import Utils.Read_Write

while False:
    #Noch adden
    Ipos=get(pos_magnetencoder)
    direction=getdirection()

start=time.time()
print(start)
while time.time()-start<20:
#for i in range(0, 200):
    #print(i)
    Iris=Utils.Read_Write.Iris()
    Iris.update_values(random.randint(0,100),"up")
    time.sleep(0.1)
    #print(Iris.get("Pos"),time.time()-start)
  
Iris.close()