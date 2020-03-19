
from PyEntity.PyEntityMain import *
from PyEntity.modules.Scene import *
from PyEntity.modules.Components import BaseComponent

Globals.debugMode = True

class PlayerController(BaseComponent.BaseComponent):
    def __init__(self):
        super().__init__()
        self.name = "PlayerController"
    def Update(self):
        pass
        #self.parent.position = Globals.mousePosition

RegisterComponent(PlayerController())

testScene = Scene("Testing",True)

particles = GameObject("System")
particles.AddComponent("PlayerController")
particles.AddComponent("ParticleSystem2D")
particles.position = Vector2(400,300)
testScene.AddObject(particles)


gameData = FullGameData()
gameData.scenes.append(testScene)
gameData.defaultScene = 0
gameData.name = "ParticleExample"
gameData.screenSize = Vector2(800, 600)

LaunchGame(gameData)


