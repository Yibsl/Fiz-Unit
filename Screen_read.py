import sqlite3
import json
import random
import time
import Utils.Read_Write


Sc=Utils.Read_Write.Screen()

start=time.time()
print(start)
while time.time()-start<20:
#while True:
    #On+=1
    #if True:
    sample_data = Sc.collect_data()
    Sc.update(sample_data)
    Sc.print_all_values()
    #time.sleep(1)


