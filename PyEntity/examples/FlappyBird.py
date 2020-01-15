from PyEntity import *
from PyEntity.PyEntityMain import *
from PyEntity.modules.Components.BaseComponent import *


class PlayerController(BaseComponent):
    def __init__(self):
        super().__init__()
        self.name = "PlayerController"
    def Update(self):
        print("KD: ", Globals.keydown)
        print("KP: ", Globals.keypressed)
        print("KU: ", Globals.keyup)
        for event in Globals.keydown:
            if(event == "w"):
                self.parent.GetComponent("Physics2D").AddVelocity(Vector2(0,-0.25))

RegisterComponent(PlayerController())

flappyScene = Scene("FlappyScene",True)

bird = GameObject("bird")
bird.tag = "player"
bird.AddComponent("PlayerController")
bird.AddComponent("Collider2D")
bird.AddComponent("Physics2D")
bird.AddComponent("Renderer2D")
bird.GetComponent("Renderer2D").sprite = Image(Globals.engineLocation+"\\assets\\Examples\\flappy.png")

flappyScene.AddObject(bird)

gameData = FullGameData()
gameData.scenes.append(flappyScene)
gameData.defaultScene = 0
gameData.name = "PhysicsTest1"
gameData.screenSize = Vector2(800, 600)
gameData.gravity = -0.5

LaunchGame(gameData)


