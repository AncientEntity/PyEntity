from PyEntity import Globals, PyEntityMain
from PyEntity.PyEntityMain import *
from PyEntity.modules.GameObject import GameObject
import copy


class Scene:
    def __init__(self, name, defaultCamera=True):
        self.name = name
        self.objects = []
        self.defaultCamera = None
        if (defaultCamera == True):
            defaultCam = GameObject("DefaultCamera")
            defaultCam.AddComponent("Camera")
            defaultCam.tag = "DefaultCamera"
            self.defaultCamera = defaultCam
            self.objects.append(defaultCam)
            Globals.mainCamera = self.defaultCamera
        # Globals.scenes.append(self)

    def AddObject(self, obj):
        if isinstance(obj, GameObject):
            self.objects.append(obj)

    def LoadScene(scene):
        LoadScene(scene)


def LoadScene(scene):
    if isinstance(scene, int):
        scene = Globals.scenes[scene]

    Globals.objects = []
    Globals.objects = copy.deepcopy(scene.objects)
    if(PyEntityMain.FindComponent("Camera") != None):
        Globals.mainCamera = PyEntityMain.FindComponent("Camera").parent
