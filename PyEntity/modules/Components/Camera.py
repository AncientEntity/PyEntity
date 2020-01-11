from PyEntity import Globals
from PyEntity.modules.Components.BaseComponent import BaseComponent
from PyEntity.modules.Vectors import Vector2
from ...PyEntityMain import *

class Camera(BaseComponent):
    def __init__(self):
        super().__init__()
        self.name = "Camera"
        self.dev = False
    def Update(self):
        if(self.dev == True):
            for event in Globals.inputEvents:
                if (event.key == "i"):
                    self.parent.position.y -= 5
                elif (event.key == "k"):
                    self.parent.position.y += 5
                if (event.key == "j"):
                    self.parent.position.x -= 5
                elif (event.key == "l"):
                    self.parent.position.x += 5
    def ScreenToWorldPoint(self,screenPoint):
        cam = FindGameObjectByTag("DefaultCamera")
        camPos = [cam.position[0], cam.position[1]]
        return ([screenPoint[0] + camPos[0], screenPoint[1] + camPos[1]])