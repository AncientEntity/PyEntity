
import random

def SelectOne(items):
    if(isinstance(items, list) == False):
        return items
    else:
        return items[random.randint(0,len(items)-1)]
