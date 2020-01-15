import sys, os

from PyEntity.modules.Image import Image

sys.path.append(os.path.join(os.path.dirname(__file__), "lib"))
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import random
import time
from PyEntity.modules.GameObject import GameObject
from PyEntity import Globals, Input
from PyEntity.modules.Scene import *
from PyEntity.modules.Vectors import *
from PyEntity.modules.RenderingManager import *
import PyEntity.Input

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
    Globals.gravity = gameData.gravity
    fCountStart = 0
    while gameRunning:
        Globals.frames+=1
        frameStartTime = time.time()
        GatherInputs()
        DoGameObjectFunctions()
        RenderEngine(Globals.screen)
        Globals.deltaTime = time.time() - frameStartTime
        Globals.gameTime += Globals.deltaTime
        #print(1.0 / Globals.deltaTime)

class FullGameData:
    def __init__(self):
        self.scenes = []
        self.defaultScene = 0
        self.name = ""
        self.screenSize = Vector2(800,600)
        self.gravity = -9.8


def GatherInputs():
    #newInputs = []
    #print(Globals.inputEvents)
    for key in Globals.keydown:
        if(key not in Globals.keypressed):
            Globals.keypressed.append(key)
    Globals.keydown = []
    Globals.keyup = []
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if(pygame.key.name(event.key) not in Globals.keypressed):
                Globals.keydown.append(pygame.key.name(event.key))
        elif event.type == pygame.KEYUP:
            if(pygame.key.name(event.key) in Globals.keypressed):
                Globals.keypressed.remove(pygame.key.name(event.key))
                Globals.keyup.append(pygame.key.name(event.key))
        elif(event.type == pygame.QUIT):
            pygame.quit()
            exit(0)
    #Globals.inputEvents = pygame.event.get()
    Globals.mousePosition = [pygame.mouse.get_cursor()[0],pygame.mouse.get_cursor()[1]]

def DoGameObjectFunctions():
    for obj in Globals.objects:
        if obj.active == False:
            continue

        scaleChange = (obj.scale != obj.lastScale)
        rotationChange = (obj.rotation != obj.lastRotation)
        for component in obj.components:
            if component.doneStart == False:
                component.Start()
                component.doneStart = True
            component.Update()
            if(scaleChange == True):
                component.ScaleChange(obj.lastScale,obj.scale)
            if(rotationChange == True):
                component.RotationChange(obj.lastRotation,obj.rotation)
        if(scaleChange == True):
            obj.lastScale = obj.scale
        if(rotationChange == True):
            obj.lastRotation = obj.rotation



def RegisterComponent(component):
    Globals.masterComponents.append(component)

def Instantiate(obj):
    new = obj.Clone()
    Globals.objects.append(new)
    return new

def FindGameObjectByTag(tag,multi=False):
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
def FindGameObjectByName(name,multi=False):
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

def FindComponents(type):
    found = []
    for obj in Globals.objects:
        for comp in obj.components:
            if(comp.name == type):
                found.append(comp)
    return found


def AllGameObjects():
    return Globals.objects

def QuitGame():
    pygame.quit()
    exit(0)
