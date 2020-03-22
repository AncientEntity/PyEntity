
import PyEntity
from PyEntity.modules.Vectors import *
from PyEntity import Globals
from PyEntity.modules import Color
import pygame
from . import DebugTools

def RenderEngine(screen):
    screen.fill((255,255,255))
    offset = Globals.mainCamera.position
    renderRequests = Globals.renderRequests
    renderRequests.sort(key=lambda x: x.sortingLayer)
    for request in renderRequests:
        workingImage = ""
        workingImage = Globals.loadedImages[request.sprite]
        #if(request.isEngineSprite == False):
        #    workingImage = Globals.loadedImages[request.sprite]
        #else:
        #    workingImage = Globals.engineSprites[request.sprite]
        imageDimensions = Vector2(0, 0)
        imageDimensions.x = workingImage.get_width()
        imageDimensions.y = workingImage.get_height()


        if(request.size != [1,1]):
            workingImage = pygame.transform.scale(workingImage,[int(imageDimensions.x * request.size[0]),int(imageDimensions.y * request.size[1])])
        imageDimensions.x = workingImage.get_width()
        imageDimensions.y = workingImage.get_height()
        if(request.color != None):
            workingImage.fill((request.color.r,request.color.g,request.color.b,request.color.a),special_flags=pygame.BLEND_MIN)
            #print(request.color)
        if (request.isUI == False):
            blitPos = (request.position.x-offset.x+(Globals.screenSize.x / 2)-(imageDimensions.x/2), request.position.y-offset.y+(Globals.screenSize.y / 2)-(imageDimensions.y/2))
            if((blitPos[0] > -imageDimensions.x and blitPos[0] < Globals.screenSize.x) and (blitPos[1] > -imageDimensions.y and blitPos[1] < Globals.screenSize.y)):
                # Make it only render objects on screen
                screen.blit(workingImage, blitPos)
        else:
            if(request.position.x >= 0 and request.position.x <= Globals.screenSize.x):
                if(request.position.y >= 0 and request.position.y <= Globals.screenSize.y):
                    # Make it only render objects on screen
                    screen.blit(workingImage, (request.position.x,request.position.y))

    pygame.display.update()
    Globals.renderRequests = []
    renderRequests = []



class RenderRequest:
    def __init__(self,sprite,position,parent,sortingLayer=0,isUI=False,engineSprite=False):
        self.sprite = sprite
        self.position = position
        self.isUI = isUI
        self.sortingLayer = sortingLayer
        self.parent = parent
        #self.isEngineSprite = engineSprite
        self.color = None
        self.size = [1,1]


