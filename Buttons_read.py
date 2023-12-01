import random
import Utils.Read_Write
import time

Button=Utils.Read_Write.Button()

for i in range(0, 200):
    #print(i)
    for x in range(1,5):
        state=random.randint(0,1)
        Button.store_button_state(x,state)
    print(Button.read_all_button_states())
    #time.sleep(0.1)
Button.close ()