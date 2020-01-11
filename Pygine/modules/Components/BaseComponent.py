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
        return copy.copy(self)

    def Start(self):
        pass

    def Update(self):
        pass
