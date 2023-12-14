import numpy as np

class MobT:
    def __init__(self,a,b,c,d) -> None:
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    
    def inverse(self):
        return MobT(self.d,-self.b,-self.c,self.a)

    def aply(self,z):
        if self.c == 0 and z == "inf":
            return "inf"
        if self.c != 0:
            if z == "inf":
                return self.a/self.b
            if z == -self.d/self.c:
                return "inf"
        return (self.a*z+self.b)/(self.c*z+self.d)
    
    def mapCircle(self, center, radius):
        # step 1
        center += self.d/self.c

        # step 2
        temp = center
        center = np.conj(center) / (abs(center)**2 - radius**2)
        radius /= abs(abs(temp)**2 - radius**2)

        # step 3
        e = (self.b*self.c - self.a*self.d)/self.c**2
        center *= e
        radius *= abs(e)

        # step 4
        center += self.a/self.c

        return (center, radius)
