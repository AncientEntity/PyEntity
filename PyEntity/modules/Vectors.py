import math


class Vector2:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    def __add__(self, other):
        return (self.x+other.x,self.y+other.y)
    def __str__(self):
        return str(self.x) + "," + str(self.y)


class Vector3:
    def __init__(self,x=0,y=0,z=0):
        self.x = x
        self.y = y
        self.z = z

def Distance2D(v1,v2):
    return math.fabs(math.sqrt((math.pow(v1.x-v2.x,2)+math.pow(v1.y-v2.y,2))))