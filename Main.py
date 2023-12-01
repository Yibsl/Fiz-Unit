import time
import Utils.Screen.Builder
from Debug import *

status="main"
x=0
Screen=Utils.Screen.Builder.builder()


while status!="off":
    x+=1
    #print(x)
    time.sleep(0.1)
    if x>1000:
        status="off"
    if status=="main":
        Screen.main()
        debug(2,"screen")

        