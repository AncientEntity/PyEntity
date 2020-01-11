import random

import Pygine.PygineMain as Pygine
from Pygine import Globals, Input
from Pygine.modules import Vectors
from Pygine.modules.Components.BaseComponent import BaseComponent
from Pygine.modules.GameObject import GameObject
from Pygine.modules.Image import Image
from Pygine.modules.Scene import Scene

class PlayerController(BaseComponent):
    def __init__(self):
        super().__init__()
        self.name = "PlayerController"
    def Update(self):
        for event in Globals.inputEvents:
            if(event.type == Input.KeyDown):
                if(event.key == "w"):
                    self.parent.position.y -= 3
                if(event.key == "s"):
                    self.parent.position.y += 3
                if(event.key == "a"):
                    self.parent.position.x -= 3
                if(event.key == "d"):
                    self.parent.position.x += 3

Pygine.RegisterComponent(PlayerController())

testScene = Scene("Testing",False)

worldSize = random.randint(8,20)
for x in range(-25,25):
    for y in range(-25,25):
        groundTile = GameObject("GTile")
        groundTile.AddComponent("SpriteRenderer")
        if(Vectors.Distance2D(Pygine.Vector2(x,y), Pygine.Vector2(0, 0)) <= worldSize):
            groundTile.GetComponent("SpriteRenderer").sprite = Image(Globals.engineLocation+"\\assets\\Examples\\grass.png")
        elif(Vectors.Distance2D(Pygine.Vector2(x,y), Pygine.Vector2(0, 0)) <= worldSize+2):
            groundTile.GetComponent("SpriteRenderer").sprite = Image(Globals.engineLocation+"\\assets\\Examples\\sand.png")
        else:
            groundTile.GetComponent("SpriteRenderer").sprite = Image(Globals.engineLocation + "\\assets\\Examples\\water.png")
        groundTile.position = Pygine.Vector2(x * 32, y * 32)
        testScene.AddObject(groundTile)

spriteTest = GameObject("Testing")
spriteTest.AddComponent("SpriteRenderer")
spriteTest.GetComponent("SpriteRenderer").sprite = Globals.errorImage
spriteTest.position = Pygine.Vector2(50, 100)
spriteTest.AddComponent("PlayerController")
spriteTest.AddComponent("Camera")
testScene.AddObject(spriteTest)
spriteTest.GetComponent("Camera").dev = True
testScene.defaultCamera = spriteTest

gameData = Pygine.FullGameData()
gameData.scenes.append(testScene)
gameData.defaultScene = 0
gameData.name = "TestGame1"
gameData.screenSize = Pygine.Vector2(800, 600)

Pygine.LaunchGame(gameData)



