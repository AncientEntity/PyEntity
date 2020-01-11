import sys, os

from Pygine.modules.Image import Image

sys.path.append(os.path.join(os.path.dirname(__file__), "lib"))
import pygame
import random
import time
from Pygine.modules.GameObject import GameObject
from Pygine import Globals, Input
from Pygine.modules.Scene import Scene
from Pygine.modules.Vectors import *
import Pygine.Input

Globals.Init()
pygame.init()
#pygame.key.set_repeat(50,50)


Globals.engineLocation = os.path.join(os.path.dirname(__file__))
Globals.errorImage = Image(Globals.engineLocation+"\\assets\\error.png")
print("Engine Loaded At: "+Globals.engineLocation)

def LaunchGame(gameData):
    Globals.scenes = gameData.scenes
    Scene.LoadScene(gameData.defaultScene)
    gameRunning = True
    Globals.screenSize = gameData.screenSize
    Globals.screen = pygame.display.set_mode((Globals.screenSize.x, Globals.screenSize.y))
    gameTime = 0
    deltaTime = 0
    frames = 0
    fCountStart = 0
    while gameRunning:
        frames+=1
        frameStartTime = time.time()
        GatherInputs()
        DoGameObjectFunctions()
        RenderEngine(Globals.screen)
        deltaTime = time.time() - frameStartTime
        gameTime += deltaTime

class FullGameData:
    def __init__(self):
        self.scenes = []
        self.defaultScene = 0
        self.name = ""
        self.screenSize = Vector2(800,600)


def GatherInputs():
    #newInputs = []
    #print(Globals.inputEvents)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            found = False
            for e in Globals.inputEvents:
                if(e.key == pygame.key.name(event.key)):
                    found = True
                    break
            if(found == False):
                Globals.inputEvents.append(Input.Event(pygame.key.name(event.key),event.type))
        elif event.type == pygame.KEYUP:
            found = None
            for e in Globals.inputEvents:
                if(e.key == pygame.key.name(event.key)):
                    found = e
                    break
            if(found != None):
                Globals.inputEvents.remove(found)
        elif(event.type == pygame.QUIT):
            pygame.quit()
            exit(0)
    #Globals.inputEvents = pygame.event.get()
    Globals.mousePosition = [pygame.mouse.get_cursor()[0],pygame.mouse.get_cursor()[1]]

def DoGameObjectFunctions():
    for obj in Globals.objects:
        if obj.active == False:
            continue
        for component in obj.components:
            if component.doneStart == False:
                component.Start()
                component.doneStart = True
            component.Update()

def RenderEngine(screen):
    screen.fill((255,255,255))
    offset = Globals.mainCamera.position
    #print(offset.x,offset.y)
    for obj in Globals.objects:
        if obj.GetComponent("SpriteRenderer") != None:
            imageDimensions = Vector2(0,0)
            imageDimensions.x = Globals.loadedImages[obj.GetComponent("SpriteRenderer").sprite].get_width()
            imageDimensions.y = Globals.loadedImages[obj.GetComponent("SpriteRenderer").sprite].get_height()
            blitPos = (obj.position.x-offset.x+(Globals.screenSize.x / 2)-(imageDimensions.x/2), obj.position.y-offset.y+(Globals.screenSize.y / 2)-(imageDimensions.y/2))
            if((blitPos[0] > -imageDimensions.x and blitPos[0] < Globals.screenSize.x) and (blitPos[1] > -imageDimensions.y and blitPos[1] < Globals.screenSize.y)):
                screen.blit(Globals.loadedImages[obj.GetComponent("SpriteRenderer").sprite], blitPos)
            # Make it only render objects on screen
    pygame.display.update()


def RegisterComponent(component):
    Globals.masterComponents.append(component)

def Instantiate(obj):
    new = obj.Clone()
    Globals.objects.append(new)
    return new

def ByTag(tag,multi=False):
    all = []
    for obj in Globals.objects:
        if(obj.tag == tag):
            if(multi == False):
                return obj
            else:
                all.append(obj)
    if(multi == False):
        return None
    else:
        return all
def ByName(name,multi=False):
    all = []
    for obj in Globals.objects:
        if(obj.name == name):
            if(multi == False):
                return obj
            else:
                all.append(obj)
    if(multi == False):
        return None
    else:
        return all
def FindComponent(type):
    for obj in Globals.objects:
        for comp in obj.components:
            if(comp.name == type):
                return comp
    return None
def All():
    return Globals.objects


