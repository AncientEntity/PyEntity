from PyEntity import Globals
from PyEntity.modules.Vectors import Vector2
import copy

class GameObject:
    def __init__(self, name):
        self.active = True
        self.name = name
        self.tag = ""
        self.position = Vector2(0,0)
        self.scale = Vector2(1,1)
        self.rotation = 0
        self.lastRotation = 0
        self.lastScale = Vector2(1,1)
        self.components = []
    def AddComponent(self,component):
        masterComponents = Globals.masterComponents
        for comp in masterComponents:
            if(comp.name == component):
                new = comp.CreateNew()
                new.parent = self
                self.components.append(new)
                return
        raise Exception(component+" is not a valid component. Make sure to register it! using RegisterComponent(component)")

    def GetComponent(self,component):
        for comp in self.components:
            if(comp.name == component):
                return comp
        return None
    def Clone(self):
        return copy.deepcopy(self)
