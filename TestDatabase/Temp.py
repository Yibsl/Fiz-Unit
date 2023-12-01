import pygame as pg

class builder:
    def __init__(self):
        self.SCREEN_WIDTH = 400
        self.SCREEN_HEIGHT = 600
        pg.init()
        self.screen = pg.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pg.display.set_caption("FIZ Screen")
        clock=pg.time.Clock()

    def main(self):
        pg.draw.rect(self.screen,(0,255,0),(-1,90,51,420),1)