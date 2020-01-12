from PyEntity.modules.Components.BaseComponent import BaseComponent
from PyEntity.modules.Components.BaseComponent import BaseComponent
from PyEntity.modules.Components.Camera import Camera
from PyEntity.modules.Components.Renderer2D import Renderer2D
from PyEntity.modules.Components.UIText import UIText
from PyEntity.modules.Components.Physics2D import Physics2D
from PyEntity.modules.Components.Collider2D import Collider2D
from PyEntity.modules.Vectors import Vector2

masterComponents = []
screen = None
renderRequests = []
screenSize = Vector2(0,0)
scenes = []
objects = []
mainCamera = None
inputEvents = []
mousePosition = [0,0]
engineLocation = ""
loadedImages = []
loadedImageLocations = []
gravity = -9.8
fpsMax = 60.0
debugMode = False

gameTime = 0
deltaTime = 0
frames = 0

errorImage = ""

def Init():
    global masterComponents
    global screen
    global objects
    global scenes
    global mainCamera
    global inputEvents
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
    mousePosition = [0,0]
    engineLocation = ""
    gravity = gravity
    masterComponents.append(BaseComponent())
    masterComponents.append(Renderer2D(None))
    masterComponents.append(Camera())
    masterComponents.append(UIText())
    masterComponents.append(Physics2D())
    masterComponents.append(Collider2D())

