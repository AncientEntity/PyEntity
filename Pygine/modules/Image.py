import pygame

from Pygine import Globals


def Image(img):
    Globals.loadedImages.append(pygame.image.load(img))
    return len(Globals.loadedImages)-1

