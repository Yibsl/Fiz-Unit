import Utils.Read_Write

#Transmit values from Screen_Database to motors
class Transmit:
    def __init__(self):
        self.Screen=Utils.Read_Write.Screen()

    def send(self):
        data=self.Screen.get_all_values()
        #transmitt data

    def recive(self):
        #recieve data from tranciver
        pass
