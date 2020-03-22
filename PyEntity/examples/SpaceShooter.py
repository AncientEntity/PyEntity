
from PyEntity.PyEntityMain import *
from PyEntity.modules.Scene import *
from PyEntity.modules.Components import BaseComponent

Globals.debugMode = True


mainScene = Scene("Main")


class PlayerController(BaseComponent.BaseComponent):
    def __init__(self):
        super().__init__()
        self.name = "PlayerController"
        self.movementSpeed = 1.2
        self.missilePrefab = None
    def Start(self):
        self.parent.tag = "Player"
    def Update(self):
        for event in Globals.keypressed:
            #print(event)
            if(event == "w"):
                self.parent.position.y -= self.movementSpeed
            elif(event == "s"):
                self.parent.position.y += self.movementSpeed
            if (event == "a"):
                self.parent.position.x -= self.movementSpeed
            elif(event == "d"):
                self.parent.position.x += self.movementSpeed
        for event in Globals.keydown:
            if(event == "space"):
                m = Instantiate(self.missilePrefab)
                m.position = Vector2(self.parent.position.x,self.parent.position.y)
        c = self.GetComponent("Collider2D").CollidingWithTagOf("missile")
        if(c != None and c.GetComponent("Missile").isPlayers == False):
            self.parent.Destroy()


class Missile(BaseComponent.BaseComponent):
    def __init__(self):
        super().__init__()
        self.name = "Missile"
        self.isPlayers = True
        self.speed = 1.5
    def Start(self):
        self.parent.tag = "missile"
    def Update(self):
        self.parent.position.y -= self.speed
        #print(self.parent.tag)


PyEntityMain.RegisterComponent(Missile())
PyEntityMain.RegisterComponent(PlayerController())





missile = GameObject("Missile Prefab")
missile.AddComponent("Missile")
missile.AddComponent("Renderer2D")
missile.GetComponent("Renderer2D").sprite = Image(Globals.engineLocation + "\\assets\\apple.png")
missile.AddComponent("Collider2D")
missile.GetComponent("Collider2D").BoundToImage()
missile.scale = Vector2(1,2)

apple = GameObject("Apple")
apple.AddComponent("Renderer2D")
apple.GetComponent("Renderer2D").sprite = Image(Globals.engineLocation + "\\assets\\apple.png")
apple.AddComponent("Collider2D")
apple.AddComponent("PlayerController")
apple.scale = Vector2(3,3)
apple.GetComponent("Collider2D").BoundToImage()
apple.position.y = 200
apple.GetComponent("PlayerController").missilePrefab = missile
apple.AddComponent("ParticleSystem2D")
p = apple.GetComponent("ParticleSystem2D")
p.randomColor = [Color.Color(226,88,34,255),Color.Color(255,88*2,34*2,255)]
p.gravity = 0.05
p.emissionBox = [-10,10,10,15]
p.particleLifetime = 30

background = GameObject("Background")
background.AddComponent("Renderer2D")
background.GetComponent("Renderer2D").sprite = Image(Globals.engineLocation+"\\assets\\Examples\\spiral-galaxy.jpg")
background.GetComponent("Renderer2D").sortingLayer = -100

mainScene.AddObject(apple)
mainScene.AddObject(background)
#mainScene.AddObject(missile)
#apple.AddComponent("Camera")


gameData = FullGameData()
gameData.scenes.append(mainScene)
gameData.defaultScene = 0
gameData.name = "Space Shooter GOT EM"
gameData.screenSize = Vector2(800, 600)

LaunchGame(gameData)


