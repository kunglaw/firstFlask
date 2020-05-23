from math import pi

class Lingkaran:

    def __init__(self,r):
        
        self.radius = r

    def setRadius(self, r):
        self.radius = r

    def getRadius(self):
        return self.radius

    def hitungLuas(self):
        return pi * (self.radius * self.radius)

    def hitungKeliling(self):
        return pi * 2 * self.radius
    
