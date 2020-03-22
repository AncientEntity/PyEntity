


class Color:
    def __init__(self,r,g,b,a=255):
        self.r = r
        self.g = g
        self.b = b
        self.a = a
    def __str__(self):
        return "("+str(self.r)+","+str(self.g)+","+str(self.b)+","+str(self.a)+")"