
from PyEntity.PyEntityMain import *
from PyEntity.modules.Scene import *

testScene = Scene("Testing")

ground = GameObject("Ground")
ground.AddComponent("Renderer2D")
ground.GetComponent("Renderer2D").sprite = Image(Globals.engineLocation + "\\assets\\Examples\\ground.png")
ground.scale.x = 8
ground.scale.y = 10
ground.position.y = 255
testScene.AddObject(ground)

apple = GameObject("Apple")
apple.AddComponent("Renderer2D")
apple.GetComponent("Renderer2D").sprite = Image(Globals.engineLocation + "\\assets\\apple.png")
apple.AddComponent("Physics2D")
apple.position.y = -100

testScene.AddObject(apple)

gameData = FullGameData()
gameData.scenes.append(testScene)
gameData.defaultScene = 0
gameData.name = "PhysicsTest1"
gameData.screenSize = Vector2(800, 600)

LaunchGame(gameData)


