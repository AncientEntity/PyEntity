from PyEntity.modules.Components.BaseComponent import BaseComponent
from PyEntity import Globals
from ..RenderingManager import RenderRequest
from .. import Image
from .. import Color
from .. import Vectors
from .. import QuickMethods
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
        self.timeAlive = 0

class ParticleSystem2D(BaseComponent):
    def __init__(self,):
        super().__init__()
        self.name = "ParticleSystem2D"
        self.sortingLayer = 0
        self.playOnAwake = True
        self.isPlaying = False
        self.particles = []
        self.maxParticles = 2500
        self.emissionSpeed = 60
        self.emissionBox = [0,0,0,0] #x,y,w,h
        self.particleLifetime = 60 # in frames
        self.randomStartVelocity = [Vectors.Vector2(-0.5,-0.5),Vectors.Vector2(0.5,0.5)] #min,max
        self.randomColor = [Color.Color(0,0,0,0),Color.Color(0,0,0,0)] #min max
        self.randomStartSize = [1,1] #min max
        self.sizeDecreaseOverTime = 0.0
        #self.particleColor = Color.Color(255,0,0,255)
        self.gravity = 0
        self.particleSprite = Image.Image("..\\assets\\default-particle.png")

        self.amountDue = 0
    def Start(self):
        if(self.playOnAwake):
            self.isPlaying = True
    def Update(self):
        for particle in self.particles: #Do current particles
            #print(particle)
            finalizedSprite = ""
            rr = RenderRequest(finalizedSprite,particle.position,self,self.sortingLayer)

            finalizedSprite = particle.sprite

            #Add color
            rr.color = particle.color
            rr.sprite = finalizedSprite
            rr.size = [particle.size,particle.size]

            Globals.renderRequests.append(rr)
            particle.timeAlive+=Globals.deltaTime
            if(particle.timeAlive >= self.particleLifetime):
                self.particles.remove(particle)
            else:
                particle.velocity.y += self.gravity * Globals.deltaTime
                particle.position.x += particle.velocity.x * Globals.deltaTime
                particle.position.y += particle.velocity.y * Globals.deltaTime
                particle.size = MathF.Clamp(particle.size - self.sizeDecreaseOverTime * Globals.deltaTime, 0.01,9999999)
        if(self.isPlaying):
            self.amountDue += self.emissionSpeed * Globals.deltaTime
            if(self.amountDue >= 1):
                for i in range(int(self.amountDue)): #Make new particles
                    if(len(self.particles) >= self.maxParticles):
                        break

                    newPos = Vectors.Vector2(self.parent.position.x+random.uniform(self.emissionBox[0],self.emissionBox[2])
                                             ,self.parent.position.y+random.uniform(self.emissionBox[1],self.emissionBox[3]))
                    newParticle = SingleParticle(newPos)
                    newParticle.velocity = Vectors.Vector2(random.uniform(self.randomStartVelocity[0].x,self.randomStartVelocity[1].x),
                                                                          random.uniform(self.randomStartVelocity[0].y,
                                                                                         self.randomStartVelocity[1].y))
                    newParticle.size = random.uniform(self.randomStartSize[0],self.randomStartSize[1])

                    newParticle.color = Color.Color(random.randint(self.randomColor[0].r,self.randomColor[1].r),
                                                    random.randint(self.randomColor[0].g, self.randomColor[1].g),
                                                    random.randint(self.randomColor[0].b, self.randomColor[1].b),
                                                    random.randint(self.randomColor[0].a, self.randomColor[1].a))
                    newParticle.sprite = QuickMethods.SelectOne(self.particleSprite)

                    self.particles.append(newParticle)
                self.amountDue = 0
