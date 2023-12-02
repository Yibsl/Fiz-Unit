import subprocess
from multiprocessing import Process

def run_Focus():
    subprocess.call(["python", "Focus_read.py"])
def run_Iris():
    subprocess.call(["python", "Iris_read.py"])
def run_Zoom():
    subprocess.call(["python", "Zoom_read.py"])
def run_Buttons():
    subprocess.call(["python", "Button_read.py"])
def run_Screen():
    subprocess.call(["python", "Screen_read.py"])
def run_Main():
    subprocess.call(["python", "Main.py"])

if __name__ == "__main__":

    # Prozesse für beide Skripte erstellen
    p1 = Process(target=run_Focus)
    p2 = Process(target=run_Iris)
    p3 = Process(target=run_Zoom)
    p4 = Process(target=run_Buttons)
    p5 = Process(target=run_Screen)
    p6 = Process(target=run_Main)

    # Prozesse starten
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p6.start()
    
print("all off")

#Komment

