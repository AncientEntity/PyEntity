
from PyEntity.PyEntityMain import *
from PyEntity.modules.Scene import *
from PyEntity.modules.Components import BaseComponent
from PyEntity.modules.Image import *

Globals.debugMode = True

class PlayerController(BaseComponent.BaseComponent):
    def __init__(self):
        super().__init__()
        self.name = "PlayerController"
        self.fpsText = None
    def Start(self):
        pass
        #self.fpsText = FindGameObjectByTag("FPS").GetComponent("UIText")
    def Update(self):
        for event in Globals.keypressed:
            if(event == "w"):
                if(self.GetComponent("Collider2D").collisionTypes['bottom'] == True):
                    self.parent.GetComponent("Physics2D").AddVelocity(Vector2(0,-1.5))
                    #print("ree")
            if (event == "a"):
                self.GetComponent("Physics2D").velocity.x -= 2 * Globals.deltaTime
                FlipImage(self.GetComponent("Renderer2D").sprite,True,False,self.parent.scale)
            elif(event == "d"):
                FlipImage(self.GetComponent("Renderer2D").sprite, False, False, self.parent.scale)
                self.GetComponent("Physics2D").velocity.x += 2 * Globals.deltaTime
        #self.fpsText.text = "FPS: "+str(round(Globals.fps))



PyEntityMain.RegisterComponent(PlayerController())

testScene = Scene("Testing",True)

ground = GameObject("Ground")
ground.AddComponent("Renderer2D")
ground.GetComponent("Renderer2D").sprite = Image(Globals.engineLocation + "\\assets\\Examples\\ground.png")
ground.AddComponent("Collider2D")
ground.GetComponent("Collider2D").BoundToImage()
ground.scale.x = 8
ground.scale.y = 10
ground.position.y = 255
testScene.AddObject(ground)

wall = GameObject("Wall")
wall.AddComponent("Renderer2D")
wall.GetComponent("Renderer2D").sprite = Image(Globals.engineLocation + "\\assets\\Examples\\ground.png")
wall.AddComponent("Collider2D")
wall.scale.x = 2
wall.scale.y = 4
wall.GetComponent("Collider2D").BoundToImage()
wall.position.y = -50
testScene.AddObject(wall)
wall2 = wall.Clone()
wall2.position.y = 150
wall3 = wall.Clone()
wall3.position.x -= 200
wall3.position.y += 150
testScene.AddObject(wall3)
wall4 = wall3.Clone()
wall4.position.x += 400
testScene.AddObject(wall4)
#testScene.RemoveObject(wall)

testScene.AddObject(wall2)


apple = GameObject("Apple")
apple.AddComponent("Renderer2D")
apple.GetComponent("Renderer2D").sprite = Image(Globals.engineLocation + "\\assets\\Examples\\player.png")
apple.scale = Vector2(0.2,0.2)
apple.AddComponent("Collider2D")
apple.AddComponent("Physics2D")
apple.AddComponent("PlayerController")
apple.GetComponent("Collider2D").BoundToImage()
apple.position.y = -200
#apple.AddComponent("Camera")

testScene.AddObject(apple)

#fpsCounter = GameObject("FPSCounter")
#fpsCounter.tag = "FPS"
#fpsCounter.x = -100
#fpsCounter.AddComponent("UIText")
#fpsCounter.GetComponent("UIText").text = "Test"
#
#testScene.AddObject(fpsCounter)

gameData = FullGameData()
gameData.scenes.append(testScene)
gameData.defaultScene = 0
gameData.name = "PhysicsTest1"
gameData.screenSize = Vector2(800, 600)

LaunchGame(gameData)


