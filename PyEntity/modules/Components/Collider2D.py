
from PyEntity.modules.Components.BaseComponent import *
import PyEntity.PyEntityMain
from PyEntity.modules.Vectors import *
from PyEntity.modules.RenderingManager import *
from PyEntity.modules import MathF
import pygame

class Collider2D(BaseComponent):
    def __init__(self):
        super().__init__()
        self.name = "Collider2D"
        self.isTrigger = False
        self.boundingBox = BoundingBox(0,0,20,20)
        self.offset = Vector2(0,0)
        if(self.parent != None and self.parent.GetComponent("Renderer2D") != None):
            self.offset = Vector2(0-self.parent.GetComponent("Renderer2D").sprite.get_width()/2,
                                  0 - self.parent.GetComponent("Renderer2D").sprite.get_height() / 2)
        self.collidingWith = []
        self.collisionTypes = {'top':False,'bottom':False,'left':False,'right':False,'any':False}
        self.phy2D = None
        if(self.parent != None):
            self.phy2D = self.parent.GetComponent("Physics2D")
        self.debug = Globals.debugMode
        self.friction = 0.005
    def Update(self):
        self.collisionTypes = {'top': False, 'bottom': False, 'left': False, 'right': False,'any':False}
        if(self.phy2D == None):
            self.phy2D = self.parent.GetComponent("Physics2D")
        else:
            self.DoCollisions()
        if(self.debug == True):
            self.DoDebug()
    def DoCollisions(self):
        self.collisionTypes = {'top': False, 'bottom': False, 'left': False, 'right': False,'any':False}
        self.collidingWith = self.CollisionBox([self.boundingBox.w,self.boundingBox.h])
        for other in self.collidingWith:
            self.collisionTypes['any'] = True

            selfB = BoundingBox(self.GetColliderData())
            otherB = BoundingBox(other.GetColliderData())

            #Check Top
            if ((selfB.x >= otherB.x and selfB.x <= otherB.x + otherB.w) or (selfB.x+selfB.w >= otherB.x and selfB.x+selfB.w <= otherB.x + otherB.w)):
                if(selfB.y >= otherB.y):
                    self.collisionTypes['top'] = True
            #Check Bottom
            if ((selfB.x >= otherB.x and selfB.x <= otherB.x + otherB.w) or (selfB.x + selfB.w >= otherB.x and selfB.x + selfB.w <= otherB.x + otherB.w)):
                if(selfB.y <= otherB.y):
                    self.collisionTypes['bottom'] = True
            #Left
            if ((selfB.y >= otherB.y and selfB.y <= otherB.y + otherB.h) or (selfB.y+selfB.h >= otherB.y and selfB.y+selfB.h <= otherB.y + otherB.h)):
                if(selfB.x + selfB.w >= otherB.x+otherB.w):
                    self.collisionTypes['right'] = True
                    print("RIGHT")
            #Right
            if ((selfB.y >= otherB.y and selfB.y <= otherB.y + otherB.h) or (selfB.y + selfB.h >= otherB.y and selfB.y + selfB.h <= otherB.y + otherB.h)):
                if(otherB.x >= selfB.x):
                    self.collisionTypes['left'] = True
                    print("LEFT")

    def DoDebug(self):
        pygame.draw.rect(Globals.screen, (255, 0, 0), pygame.Rect(self.GetColliderData()))
        pygame.display.update()
    def CollisionBox(self,size,offset="DEFAULT"):
        if(offset == "DEFAULT"):
            offset = [-size[0]/2,-size[1]/2]
        colliders = []
        for collider in PyEntity.PyEntityMain.FindComponents("Collider2D"):
            if(collider == self):
                continue
            otherData = pygame.Rect(collider.GetColliderData())
            selfData = pygame.Rect(self.GetColliderData())
            if(selfData.colliderect(otherData)):
                colliders.append(collider)
        return colliders
    def GetColliderData(self):
        scale = self.parent.scale
        offset = self.offset
        renderer = self.parent.GetComponent("Renderer2D")
        return [self.parent.position.x+(Globals.screenSize.x/2)+(offset.x*scale.x),
                self.parent.position.y+(Globals.screenSize.y/2)+(offset.y*scale.y),
                Globals.loadedImages[renderer.sprite].get_width(),
                Globals.loadedImages[renderer.sprite].get_height()]
    def BoundToImage(self):
        offset = Vector2(0,0)
        renderer = self.parent.GetComponent("Renderer2D")
        offset.x = self.parent.position.x - Globals.loadedImages[renderer.sprite].get_width() / 2
        offset.y = self.parent.position.y - Globals.loadedImages[renderer.sprite].get_height() / 2
        self.boundingBox.w = Globals.loadedImages[renderer.sprite].get_width()
        self.boundingBox.h = Globals.loadedImages[renderer.sprite].get_height()
        self.offset = offset

class BoundingBox:
    def __init__(self,x,y=0,w=0,h=0):
        self.x = 0
        self.y = 0
        self.w = 0
        self.h = 0
        if(isinstance(x,list)):
            self.x = x[0]
            self.y = x[1]
            self.w = x[2]
            self.h = x[3]
            return
        self.x = x
        self.y = y
        self.w = w
        self.h = h