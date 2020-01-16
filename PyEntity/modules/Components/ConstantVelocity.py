
from . import BaseComponent
from .. import Vectors

class ConstantVelocity(BaseComponent.BaseComponent):
    def __init__(self):
        super().__init__()
        self.name = "ConstantVelocity"
        self.constantV = Vectors.Vector2(0,0)
    def Update(self):
        self.GetComponent("Physics2D").velocity = self.constantV