import pygame as pg
from Utils.Debug import *
from Utils.Screen.Elements import *

class builder:
    def __init__(self):
        debug(1,"innit Builder")
        self.SCREEN_WIDTH = 400
        self.SCREEN_HEIGHT = 600#
        self.BackgroundColor=(0,0,0)

        pg.init()

        self.screen = pg.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pg.display.set_caption("FIZ Screen")
        clock=pg.time.Clock()
        #self.Focus=Focus(self.screen)
        self.Iris=Iris(self.screen)
        #self.Zoom=Zoom(self.screen)
        #self.Infos=Infos(self.screen)


        

    def main(self):
        debug(2,"Build Main")
        self.screen.fill(self.BackgroundColor)  # Fülle den Bildschirm mit Schwarz, um vorherige Zeichnungen zu löschen
        #self.Focus.draw()
        self.Iris.draw()
        #self.Zoom.draw(300)
        #self.Infos.draw()
        pg.display.flip()  # Aktualisiere den Bildschirm

    def menu(self):
        pass
