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


def ScaleImage(img, newScale):
    if(isinstance(img,pygame.Surface)):
        return pygame.transform.scale(img,(img.get_width() * newScale.x,img.get_height() * newScale.y))
    else:
        new = Globals.loadedImages[Image(Globals.loadedImageLocations[img])]
        new = pygame.transform.scale(new,(new.get_width() * newScale.x, new.get_height() * newScale.y))
        Globals.loadedImages[img] = new
        return img