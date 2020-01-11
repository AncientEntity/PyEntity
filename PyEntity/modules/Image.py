import pygame

from PyEntity import Globals


def Image(img,override=-1):
    if(isinstance(img,pygame.Surface)):
        if(override == -1):
            Globals.loadedImages.append(img)
        else:
            Globals.loadedImages[override] = img
        Globals.loadedImageLocations.append("runtime")
        return len(Globals.loadedImages) - 1
    if(img in Globals.loadedImageLocations):
        return Globals.loadedImageLocations.index(img)
    if(override == -1):
        Globals.loadedImages.append(pygame.image.load(img))
    else:
        Globals.loadedImages[override] = pygame.image.load(img)
    Globals.loadedImageLocations.append(img)
    return len(Globals.loadedImages)-1

