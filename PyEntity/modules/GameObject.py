from PyEntity import Globals
from PyEntity.modules.Vectors import Vector2

class GameObject:
    def __init__(self, name):
        self.active = True
        self.name = name
        self.tag = ""
        self.position = Vector2()
        self.components = []

    def AddComponent(self,component):
        masterComponents = Globals.masterComponents
        for comp in masterComponents:
            if(comp.name == component):
                new = comp.CreateNew()
                new.parent = self
                self.components.append(new)

    def GetComponent(self,component):
        for comp in self.components:
            if(comp.name == component):
                return comp
        return None
    def Clone(self):
        return copy.copy(self)
