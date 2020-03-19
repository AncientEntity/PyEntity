from PyEntity import *
from PyEntity.PyEntityMain import *
from PyEntity.modules.Components.BaseComponent import *


class PlayerController(BaseComponent):
    def __init__(self):
        super().__init__()
        self.name = "PlayerController"
        self.timer = 1.5
    def Start(self):
        self.parent.tag = "player"
    def Update(self):
        #print("KD: ", Globals.keydown)
        #print("KP: ", Globals.keypressed)
        #print("KU: ", Globals.keyup)
        for event in Globals.keydown:
            if(event == "w"):
                self.parent.GetComponent("Physics2D").velocity.y = -1
        for event in Globals.keypressed:
            if(event == "right"):
                Globals.mainCamera.position.x += 1
            if(event == "up"):
                Globals.mainCamera.position.y -= 1
            if(event == "down"):
                Globals.mainCamera.position.y += 1
        if(self.parent.position.y < -225):
            self.parent.Destroy()
        if(self.parent.position.y > 220):
            self.parent.Destroy()
        self.timer -= Globals.deltaTime
        if(self.timer <= 0):
            pipe = Instantiate(basePipe)
            topPipe = Instantiate(basePipe)
            offset = random.randint(-200,200)
            pipe.position.y = offset-435
            pipe.position.x = 800
            topPipe.position.y = offset+435
            topPipe.position.x = 800
            self.timer = 1.5
        self.DoDeath()
    def DoDeath(self):
        for other in self.GetComponent("Collider2D").collidingWith:
            if(other.parent.tag == "enemy"):
                self.parent.Destroy()


RegisterComponent(PlayerController())

flappyScene = Scene("FlappyScene",True)

bird = GameObject("bird")
bird.tag = "player"
bird.AddComponent("PlayerController")
bird.AddComponent("Collider2D")
bird.AddComponent("Physics2D")
bird.AddComponent("Renderer2D")
bird.GetComponent("Renderer2D").sprite = Image(Globals.engineLocation+"\\assets\\Examples\\flappy.png")
bird.scale = Vector2(3,3)

flappyScene.AddObject(bird)

basePipe = GameObject("Pipe")
basePipe.AddComponent("Renderer2D")
basePipe.GetComponent("Renderer2D").sprite = Image(Globals.engineLocation+"\\assets\\Examples\\pipe.png")
basePipe.AddComponent("Physics2D")
basePipe.GetComponent("Physics2D").lockedDirections.y = True
basePipe.AddComponent("Collider2D")
basePipe.position.x = 700
basePipe.AddComponent("ConstantVelocity")
basePipe.GetComponent("ConstantVelocity").constantV.x = -0.5
basePipe.tag = "enemy"
basePipe.scale = Vector2(2,3)
Globals.prefabs.append(basePipe)

gameData = FullGameData()
gameData.scenes.append(flappyScene)
gameData.defaultScene = 0
gameData.name = "PhysicsTest1"
gameData.screenSize = Vector2(800, 600)
gameData.gravity = -1.1

LaunchGame(gameData)


