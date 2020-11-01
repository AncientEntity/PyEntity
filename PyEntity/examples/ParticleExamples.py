
from PyEntity.PyEntityMain import *
from PyEntity.modules.Scene import *
from PyEntity.modules.Components import BaseComponent
from PyEntity.modules import Vectors
from PyEntity.modules.MathF import *

Globals.debugMode = True

class PlayerController(BaseComponent.BaseComponent):
    def __init__(self):
        super().__init__()
        self.name = "PlayerController"
        self.PS = None
        self.FPS = None
    def Start(self):
        self.PS = FindGameObjectByTag("PS").GetComponent("ParticleSystem2D")
        self.FPS = FindGameObjectByName("FPSCounter").GetComponent("UIText")
    def Update(self):
        #self.PS.emissionSpeed += 1
        self.FPS.text = str(int(Globals.fps))
        #self.PS.gravity = Clamp(self.PS.gravity+random.randint(-1,1),-1,1)
        self.parent.position = Globals.mouseWorldPosition
        for event in Globals.keydown:
            if(event == "space"):
                if(self.PS.useLocalSpace):
                    self.PS.useLocalSpace = False
                else:
                    self.PS.useLocalSpace = True

RegisterComponent(PlayerController())

testScene = Scene("Testing",True)

particles = GameObject("System")
particles.tag = "PS"
particles.AddComponent("PlayerController")
particles.AddComponent("ParticleSystem2D")
particles.position = Vector2(0,0)
p = particles.GetComponent("ParticleSystem2D")
p.maxParticles = 2000
p.emissionBox = [-1,-31,1,1]
p.particleLifetime = 10
p.randomStartVelocity = [Vectors.Vector2(-25,0),Vectors.Vector2(25,25)]
p.randomStartSize = [1,5]
p.sizeDecreaseOverTime = 0.01
p.randomColor = [Color.Color(226,88,34,10),Color.Color(255,88*2,34*2,255)]
p.gravity = 100
p.emissionSpeed = 25
testScene.AddObject(particles)

fpsCounter = GameObject("FPSCounter")
fpsCounter.tag = "FPS"
fpsCounter.x = -100
fpsCounter.AddComponent("UIText")
fpsCounter.GetComponent("UIText").text = "Test"

testScene.AddObject(fpsCounter)



gameData = FullGameData()
gameData.scenes.append(testScene)
gameData.defaultScene = 0
gameData.name = "ParticleExample"
gameData.screenSize = Vector2(800, 600)

LaunchGame(gameData)


