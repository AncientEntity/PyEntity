
from PyEntity.PyEntityMain import *
from PyEntity.modules.Scene import *
from PyEntity.modules.Components import BaseComponent
from PyEntity.modules import Vectors

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
particles.position = Vector2(0,0)
p = particles.GetComponent("ParticleSystem2D")
p.maxParticles = 5000
p.emissionBox = [-400,-300,400,300]
p.particleLifetime = 300
p.randomStartVelocity = [Vectors.Vector2(-1.5,-1.5),Vectors.Vector2(1.5,1.5)]
p.randomStartSize = [1,5]
p.sizeDecreaseOverTime = 0.01
p.randomColor = [Color.Color(226,88,34,255),Color.Color(255,88*2,34*2,255)]
testScene.AddObject(particles)


gameData = FullGameData()
gameData.scenes.append(testScene)
gameData.defaultScene = 0
gameData.name = "ParticleExample"
gameData.screenSize = Vector2(800, 600)

LaunchGame(gameData)


