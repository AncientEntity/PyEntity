from .Renderer2D import *
import pygame
from PyEntity.modules import Image

class UIText(Renderer2D):
    def __init__(self):
        super().__init__(None)
        self.name = "UIText"
        self.text = "New Text"
        self.font = "Comic Sans MS"
        self.size = 30
        self.offset = [0,0]
        self.requiresStart = True
        self.generatedFont = ""
        self.generatedRender = -1
        self.centered = False
        self.lastTextGenerated = ""
        self.lastTextSize = 30
        self.isUI = True
    def GenerateText(self):
        self.generatedFont = pygame.font.SysFont(self.font,self.size)
        self.generatedRender = Image.Image(self.generatedFont.render(self.text,True,(0,0,0)),self.generatedRender)
        self.lastTextGenerated = self.text
        self.lastTextSize = self.size
    def Start(self):
        self.GenerateText()
    def Update(self):
        if(self.lastTextGenerated != self.text or self.lastTextSize != self.size):
            self.GenerateText()
        Globals.renderRequests.append(RenderRequest(self.generatedRender, self.parent.position, self, self.sortingLayer,self.isUI))