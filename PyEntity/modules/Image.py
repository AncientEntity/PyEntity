import pygame

from PyEntity import Globals


def Image(img):
    Globals.loadedImages.append(pygame.image.load(img))
    return len(Globals.loadedImages)-1

