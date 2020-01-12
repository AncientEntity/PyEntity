
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
        self.collidingWith = self.CollisionBox([self.boundingBox.w,self.boundingBox.h])
        for other in self.collidingWith:
            player_bottom = self.parent.position.y + self.boundingBox.h
            tiles_bottom = other.parent.position.y + other.boundingBox.h
            player_right = self.parent.position.x + self.boundingBox.w
            tiles_right = other.parent.position.x + other.boundingBox.w

            b_collision = tiles_bottom - self.parent.position.y
            t_collision = player_bottom - other.parent.position.y
            l_collision = player_right - other.parent.position.x
            r_collision = tiles_right - self.parent.position.x

            if (t_collision < b_collision and t_collision < l_collision and t_collision < r_collision):
                self.collisionTypes['top'] = True
            if (b_collision < t_collision and b_collision < l_collision and b_collision < r_collision):
                self.collisionTypes['bottom'] = True
            if (l_collision < r_collision and l_collision < t_collision and l_collision < b_collision):
                self.collisionTypes['left'] = True
            if (r_collision < l_collision and r_collision < t_collision and r_collision < b_collision):
                self.collisionTypes['right'] = True
            self.collisionTypes['any'] = True
        #print(self.collisionTypes)
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
    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h