import cmath
i = 0+1j
pi = cmath.pi
a = 1/2
b = cmath.exp(i*4)
T = lambda z: (3*z-6)/(2*z)
#print(T(0))
print(T(1))
#print(T(-1))
print(T(3+3*i))
print((6+6*i)*(6-6*i))
def traza(a,b,c,d):
    return (a+d)/(a*d-b*c)**(1/2)
print(traza(b,a*b,a,1))