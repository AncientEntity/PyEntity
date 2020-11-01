from PyEntity.modules.Components.BaseComponent import BaseComponent
from PyEntity.modules.Components.Camera import Camera
from PyEntity.modules.Components.Renderer2D import Renderer2D
from PyEntity.modules.Components.UIText import UIText
from PyEntity.modules.Components.Physics2D import Physics2D
from PyEntity.modules.Components.Collider2D import Collider2D
from PyEntity.modules.Components.ConstantVelocity import ConstantVelocity
from PyEntity.modules.Components.ParticleSystem import ParticleSystem2D
from PyEntity.modules.Vectors import Vector2

masterComponents = []
screen = None
renderRequests = []
screenSize = Vector2(0,0)
scenes = []
objects = []
mainCamera = None
keydown = []
keypressed =[]
keyup = []
mousePosition = [0,0]
mouseWorldPosition = [0,0]
engineLocation = ""
loadedImages = []
loadedImageLocations = []
gravity = -9.8
fpsMax = 60.0
debugMode = False
prefabs = []

gameTime = 0
deltaTime = 0
frames = 0
targetFPS = 60#-1 == no limit
fps = -1

errorImage = ""
engineSprites = []

def Init():
    global masterComponents
    global screen
    global objects
    global scenes
    global mainCamera
    global keydown
    global keypressed
    global keyup
    global mousePosition
    global engineLocation
    global errorImage
    global loadedImages
    global gravity
    global fpsMax
    global screenSize
    global loadedImageLocations
    global frames
    global deltaTime
    global gameTime
    global debugMode
    global prefabs
    global engineSprites
    global targetFPS
    global fps

    fps = -1
    prefabs = []
    keydown = []
    keypressed = []
    keyup = []
    debugMode = debugMode
    frames = 0
    deltaTime = 0
    gameTime = 0
    screenSize = screenSize
    masterComponents = []
    screen = None
    objects = []
    scenes = []
    loadedImages = []
    inputEvents = []
    mainCamera = None
    fpsMax = fpsMax
    errorImage = ""
    mousePosition = Vector2(0,0)
    engineLocation = ""
    gravity = gravity

    engineSprites = []

    masterComponents.append(BaseComponent())
    masterComponents.append(Renderer2D(None))
    masterComponents.append(Camera())
    masterComponents.append(UIText())
    masterComponents.append(Physics2D())
    masterComponents.append(Collider2D())
    masterComponents.append(ConstantVelocity())
    masterComponents.append(ParticleSystem2D())

