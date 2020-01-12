from PyEntity.modules.Components.BaseComponent import BaseComponent
from PyEntity import Globals
from ... import Globals
from .. import Vectors
from .. import MathF

class Physics2D(BaseComponent):
    def __init__(self):
        super().__init__()
        self.name = "Physics2D"
        self.gravity = Globals.gravity
        self.velocity = Vectors.Vector2(0,0)
        self.rotationVelocity = 0
        self.static = False
        self.myCol = None
    def Start(self):
        self.myCol = self.parent.GetComponent("Collider2D")
    def Update(self):
        if(self.static == False):
            if(self.parent.GetComponent("Collider2D") != None):
                if(self.myCol.collisionTypes['bottom'] == True or self.myCol.collisionTypes['any']):
                    self.velocity.y = MathF.Clamp(self.velocity.y,-500,0)
            if(self.myCol.collisionTypes['bottom'] == False and  self.myCol.collisionTypes['any'] == False):
                self.velocity.y -= self.gravity * Globals.deltaTime
            else:
                self.velocity.y = 0
                if (self.velocity.x != 0):
                    self.velocity.x -= float(self.velocity.x) * 0.005
            self.parent.position = Vectors.Vector2(self.parent.position.x + self.velocity.x,
                                                   self.parent.position.y + self.velocity.y)
            #print(self.velocity)
            self.parent.rotation += self.rotationVelocity
            print(self.myCol.collisionTypes)
    def AddVelocity(self,vecToAdd):
        self.velocity.x += vecToAdd.x
        self.velocity.y += vecToAdd.y
        self.myCol.collisionTypes['bottom'] = True
        if(self.velocity.y < 0):
            self.parent.position.y -= 0.25
