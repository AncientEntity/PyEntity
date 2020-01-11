
import PyEntity
from PyEntity.modules.Vectors import *
from PyEntity import Globals
import pygame
from . import DebugTools

def RenderEngine(screen):
    screen.fill((255,255,255))
    offset = Globals.mainCamera.position
    renderRequests = Globals.renderRequests
    renderRequests.sort(key=lambda x: x.sortingLayer)
    for request in renderRequests:
        if (request.isUI == False):
            imageDimensions = Vector2(0,0)
            imageDimensions.x = Globals.loadedImages[request.sprite].get_width()
            imageDimensions.y = Globals.loadedImages[request.sprite].get_height()
            blitPos = (request.position.x-offset.x+(Globals.screenSize.x / 2)-(imageDimensions.x/2), request.position.y-offset.y+(Globals.screenSize.y / 2)-(imageDimensions.y/2))
            if((blitPos[0] > -imageDimensions.x and blitPos[0] < Globals.screenSize.x) and (blitPos[1] > -imageDimensions.y and blitPos[1] < Globals.screenSize.y)):
                # Make it only render objects on screen
                screen.blit(Globals.loadedImages[request.sprite], blitPos)
        else:
            if(request.position.x >= 0 and request.position.x <= Globals.screenSize.x):
                if(request.position.y >= 0 and request.position.y <= Globals.screenSize.y):
                    # Make it only render objects on screen
                    screen.blit(Globals.loadedImages[request.sprite], (request.position.x,request.position.y))

    pygame.display.update()
    Globals.renderRequests = []
    renderRequests = []



class RenderRequest:
    def __init__(self,sprite,position,parent,sortingLayer=0,isUI=False):
        self.sprite = sprite
        self.position = position
        self.isUI = isUI
        self.sortingLayer = sortingLayer
        self.parent = parent