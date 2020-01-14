
from PyEntity.PyEntityMain import *
from PyEntity.modules.Scene import *
from PyEntity.modules.Components import BaseComponent

Globals.debugMode = True

class PlayerController(BaseComponent.BaseComponent):
    def __init__(self):
        super().__init__()
        self.name = "PlayerController"
    def Update(self):
        for event in Globals.inputEvents:
            if(event.type == Input.KeyDown):
                if(event.key == "w"):
                    if(self.GetComponent("Collider2D").collisionTypes['bottom'] == True):
                        self.parent.GetComponent("Physics2D").AddVelocity(Vector2(0,-2.35))
                        #print("ree")
                if (event.key == "a"):
                    self.GetComponent("Physics2D").velocity.x -= 0.005
                elif(event.key == "d"):
                    self.GetComponent("Physics2D").velocity.x += 0.005


PyEntityMain.RegisterComponent(PlayerController())

testScene = Scene("Testing")

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
wall.position.y = 0
testScene.AddObject(wall)
wall2 = wall.Clone()
wall2.position.y = 150


testScene.AddObject(wall2)


apple = GameObject("Apple")
apple.AddComponent("Renderer2D")
apple.GetComponent("Renderer2D").sprite = Image(Globals.engineLocation + "\\assets\\apple.png")
apple.AddComponent("Collider2D")
apple.AddComponent("Physics2D")
apple.AddComponent("PlayerController")
apple.scale = Vector2(3,3)
apple.GetComponent("Collider2D").BoundToImage()
apple.position.y = -100

testScene.AddObject(apple)

gameData = FullGameData()
gameData.scenes.append(testScene)
gameData.defaultScene = 0
gameData.name = "PhysicsTest1"
gameData.screenSize = Vector2(800, 600)

LaunchGame(gameData)


