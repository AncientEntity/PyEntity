from .. import DebugTools
import copy

from ... import Globals


class BaseComponent:
    def __init__(self):
        self.name = "Base";
        self.doneStart = False
        self.parent = None
        # DebugTools.Debug("Don't use BaseComponent. Use it as a base.")
        Globals.masterComponents.append(self)

    def CreateNew(self):
        return copy.deepcopy(self)

    def GetComponent(self,component):
        for comp in self.parent.components:
            if(comp.name == component):
                return comp
        return None

    def Start(self):
        pass

    def Update(self):
        pass
    def ScaleChange(self,old,new):
        pass
    def RotationChange(self,old,new):
        pass
    def __str__(self):
        return self.parent.name + "<"+self.name+">"
