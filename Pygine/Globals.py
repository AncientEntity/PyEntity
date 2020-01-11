from Pygine.modules.Components.BaseComponent import BaseComponent
from Pygine.modules.Components.BaseComponent import BaseComponent
from Pygine.modules.Components.Camera import Camera
from Pygine.modules.Components.SpriteRenderer import SpriteRenderer
from Pygine.modules.Vectors import Vector2

masterComponents = []
screen = None
screenSize = Vector2(0,0)
scenes = []
objects = []
mainCamera = None
inputEvents = []
mousePosition = [0,0]
engineLocation = ""
loadedImages = []
gravity = -0.25
fpsMax = 60.0

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
    masterComponents.append(SpriteRenderer(None))
    masterComponents.append(Camera())

