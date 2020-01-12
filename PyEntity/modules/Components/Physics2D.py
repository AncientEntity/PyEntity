from PyEntity.modules.Components.BaseComponent import BaseComponent
from PyEntity import Globals
from ... import Globals
from .. import Vectors

class Physics2D(BaseComponent):
    def __init__(self):
        super().__init__()
        self.name = "Physics2D"
        self.gravity = Globals.gravity
        self.velocity = Vectors.Vector2(0,0)
        self.static = False
    def Update(self):
        if(self.static == False):
            self.velocity.y -= self.gravity * Globals.deltaTime
            self.parent.position = Vectors.Vector2(self.parent.position.x+self.velocity.x,self.parent.position.y+self.velocity.y)