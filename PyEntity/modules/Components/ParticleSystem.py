from PyEntity.modules.Components.BaseComponent import BaseComponent
from PyEntity import Globals
from ..RenderingManager import RenderRequest
from .. import Image
from .. import Color
from .. import Vectors
import random
from .. import MathF
import pygame

class SingleParticle():
    def __init__(self,position):
        self.velocity = Vectors.Vector2(0,0)
        self.position = position
        self.sprite = -1
        self.size = 1
        self.color = Color.Color(255,255,255,0)
        self.frames = 0

class ParticleSystem2D(BaseComponent):
    def __init__(self,):
        super().__init__()
        self.name = "ParticleSystem2D"
        self.sortingLayer = 0
        self.isUI = False
        self.particles = []
        self.maxParticles = 5000
        self.emmisionPerFrame = 1
        self.emissionBox = [-400,-300,400,300] #x,y,w,h
        self.particleLifetime = 300 # in frames
        self.randomStartVelocity = [Vectors.Vector2(-1.5,-1.5),Vectors.Vector2(1.5,1.5)] #min,max
        self.randomColor = [Color.Color(226,88,34,255),Color.Color(255,88*2,34*2,255)] #min max
        self.randomStartSize = [1,5] #min max
        self.sizeDecreaseOverTime = 0.01
        #self.particleColor = Color.Color(255,0,0,255)
        self.gravity = 0
    def Update(self):
        for particle in self.particles: #Do current particles
            #print(particle)
            finalizedSprite = ""
            rr = RenderRequest(finalizedSprite,particle.position,self,self.sortingLayer)
            if(particle.sprite == -1):
                finalizedSprite = 0 # The default-particle.png sprite
                rr.isEngineSprite = True
            else:
                finalizedSprite = particle.sprite

            #Add color
            rr.color = particle.color
            rr.sprite = finalizedSprite
            rr.size = [particle.size,particle.size]

            Globals.renderRequests.append(rr)
            particle.frames+=1
            if(particle.frames >= self.particleLifetime):
                self.particles.remove(particle)
            else:
                particle.velocity.y += self.gravity
                particle.position.x += particle.velocity.x
                particle.position.y += particle.velocity.y
                particle.size = MathF.Clamp(particle.size - self.sizeDecreaseOverTime, 0.01,99999)
        for i in range(self.emmisionPerFrame): #Make new particles
            if(len(self.particles) >= self.maxParticles):
                break

            newPos = Vectors.Vector2(self.parent.position.x-Globals.screenSize.x/2+random.uniform(self.emissionBox[0],self.emissionBox[2])
                                     ,self.parent.position.y-Globals.screenSize.y/2++random.uniform(self.emissionBox[1],self.emissionBox[3]))
            newParticle = SingleParticle(newPos)
            newParticle.velocity = Vectors.Vector2(random.uniform(self.randomStartVelocity[0].x,self.randomStartVelocity[1].x),
                                                                  random.uniform(self.randomStartVelocity[0].y,
                                                                                 self.randomStartVelocity[1].y))
            newParticle.size = random.uniform(self.randomStartSize[0],self.randomStartSize[1])

            newParticle.color = Color.Color(random.randint(self.randomColor[0].r,self.randomColor[1].r),
                                            random.randint(self.randomColor[0].g, self.randomColor[1].g),
                                            random.randint(self.randomColor[0].b, self.randomColor[1].b),
                                            random.randint(self.randomColor[0].a, self.randomColor[1].a))

            self.particles.append(newParticle)
