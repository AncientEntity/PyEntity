from PyEntity.modules.Components.BaseComponent import BaseComponent
from PyEntity import Globals
from ..RenderingManager import RenderRequest
from .. import Image

class Renderer2D(BaseComponent):
    def __init__(self, sprite):
        super().__init__()
        self.name = "Renderer2D"
        self.sprite = sprite
        self.sortingLayer = 0
        self.isUI = False
    def Update(self):
        if(self.sprite != None):
            Globals.renderRequests.append(RenderRequest(self.sprite,self.parent.position,self,self.sortingLayer))
    def ScaleChange(self,old,new):
        self.sprite = Image.ScaleImage(self.sprite,new)
        #print("Scale updated "+self.parent.name)
    def RotationChange(self,old,new):
        self.sprite = Image.RotateImage(self.sprite,new,self.parent.scale)