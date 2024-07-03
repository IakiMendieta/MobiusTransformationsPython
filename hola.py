import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
# ax = fig.add_subplot(projection="3d")

x=np.linspace(-1,1,30)
y=np.linspace(-1,1,30)

X,Y = np.meshgrid(x,y)

a = np.cos(np.pi/3)
b = np.sin(np.pi/3)

A=[[3,1,-2],
   [-1,2,1],
   [4,1,-3]]

u = -(Y+X*X)**2
v = 0*X
#w = 4*X+Y-3*Z

# ax.axis("equal")
# ax.set(xlim3d=(-1,1),ylim3d=(-1,1), zlim3d=(-1,1))

plt.quiver(X,Y,u,v)

# ax.quiver(X,Y,Z,u,v,w,length=0.1)

# t = np.linspace(-2,2,100)
# X = a*np.exp(3*t)-b*np.exp(4*t)
# Y = b*np.exp(4*t)+a*np.exp(3*t)
# Z = np.exp(5*t)
# ax.plot(X,Y,Z, "r")

plt.show()