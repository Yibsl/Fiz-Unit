import pygame as pg
import numpy as np
import re
import json
from Debug import *
import Utils.Read_Write


settings=Utils.Read_Write.Settings()
settings.delete("all")
settings.create()

class Text:
    def font():
        return 

    def renderText(screen, position, text, style, size,color=(0, 0, 0)):
        GAME_FONT = pg.freetype.SysFont(settings.get_by_key("Font","Screen"), 24)
        GAME_FONT.render_to(screen, position, text, color, size=size,)

    

#not working
class focus:
    def __init__(self,screen):
        debug(1,"innit Focus")
        self.screen=screen
        self.y=0
        self.offset=0
        self.FocusData={}

    def control(self,y):
        if -601==self.offset:
            self.offset=-600
        if 101==self.offset:
            self.offset=100

        self.offset+=y

    def draw(self):
        debug(2,"Draw Iris")
        scr=self.scr
        len=Screen.Focus("länge")
        width=Screen.Focus("width")
        pos=(400,100)
        self.color=Screen.Focus("color")

        hight=1000
        x_end = pos[0]
        y= pos[1]
        x_an = x_end-len
        lin=Sigma_focus.__len__()
        
        pg.draw.rect(scr,self.color,(350,90,51,420),1)

        pg.draw.line(self.scr,self.color,(400,310),(390,302),2)
        pg.draw.line(self.scr,self.color,(400,302),(390,302),2)

        pg.draw.line(self.scr,self.color,(400,298),(390,298),2)
        pg.draw.line(self.scr,self.color,(400,290),(390,298),2)

        for i in Sigma_focus.keys():
            y=i+self.offset+pos[1]
            
            if 100<y<500:
                j=Sigma_focus.get(i)
                pg.draw.line(scr, self.color, [x_an,y], [x_end,y], width)
                object.renderText(scr, [x_an-25, y], str(j),1,10,self.color)

class Iris:
    def __init__(self,screen):
        debug(1, "innit Iris")
        self.screen=screen
        
        

    def update(self):
        self.width=2
        self.len=10
        self.objektiv=False
        self.iris=Utils.Read_Write.Iris()
        self.pfeil = self.iris.get("Pos")

        c=[int(s) for s in re.findall(r'\b\d+\b', settings.get_by_key("ColorI","Screen"))]
        self.color=(c[0],c[1],c[2])
        id=settings.get_by_key("CurrentLense","Misc")
        self.iris=json.loads(settings.get_by_id("Iris","Lenses",id)[0].replace("'", '"')) #Importiert Str und wandelt es in ein Dic um



    def draw(self):
        Iris.update(self)
        pos=(10,100)
        hight=400
        x_an = pos[0]
        y= pos[1]
        x_end = x_an+self.len
        lin=self.iris.__len__()
        step=(hight/(lin-1))

    #Rectangle
        pg.draw.rect(self.screen,self.color,(-1,90,51,420),1)
    #Linien/zahlen 
        for i in self.iris.keys():
            j=self.iris.get(i)
            pg.draw.line(self.screen, self.color, [x_an,y], [x_end, y], self.width)
            Text.renderText(self.screen, [x_end+5, y], str(j),1,10,self.color)
            y+=step
    #Pfeil
        pg.draw.line(self.screen,self.color,(0,self.pfeil),(5,self.pfeil+5),5)
        pg.draw.line(self.screen,self.color,(0,self.pfeil+10),(5,self.pfeil+5),5)


class Zoom:
    def __init__(self,screen):
        debug(1,"innit Zoom")
        self.width=(400,600)
        self.screen=screen

    def update():
        self.color=Screen.Zoom("color")
        (self.color)
        self.min=Sigma_zoom.get("min")
        self.max=Sigma_zoom.get("max")
        self.size=Screen.Zoom("size")
        self.screen=screen
        self.zoom=self.min

    def draw(self,position): 

        self.zoom=position

        pg.draw.rect(self.screen,self.color,(125,500,150,101),1)
        object.renderText(self.screen, (160,520), str(self.max), 1, self.size,self.color)
        object.renderText(self.screen, (160,580), str(self.min), 1, self.size,self.color)
        object.renderText(self.screen, (210,543), str(self.zoom), 1, self.size+12,self.color)


