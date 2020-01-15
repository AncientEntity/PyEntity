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
    #if(img in Globals.loadedImageLocations and override==-1):
    #    return Globals.loadedImageLocations.index(img)
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
        if(img == None):
            return
        if(Image(Globals.loadedImageLocations[img]) == None):
            return
        new = Globals.loadedImages[Image(Globals.loadedImageLocations[img])]
        new = pygame.transform.scale(new,(int(new.get_width() * newScale.x), int(new.get_height() * newScale.y)))
        Globals.loadedImages[img] = new
        return img

def RotateImage(img, rotation,scale):
    if(isinstance(img,pygame.Surface)):
        return pygame.transform.rotate(img,rotation)
    else:
        new = Image(Globals.loadedImageLocations[img],override=img)
        Globals.loadedImages[img] = ScaleImage(pygame.transform.rotate(Globals.loadedImages[new],rotation),scale)
        return img