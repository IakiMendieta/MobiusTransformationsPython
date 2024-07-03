import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation 

figure, axes = plt.subplots()

Vector = lambda x1,x2: np.array([-x2, 
                                 x1])

x = np.linspace(-4,4,30)
y = np.linspace(-3,3,30)

X,Y = np.meshgrid(x,y)
U,V = Vector(X,Y)

axes.axis("equal")
axes.quiver(X,Y,U,V)

circle = plt.Circle((-0.5,-0.5),0.1)
axes.add_patch(circle)

def animate(frame):
    h = 0.03
    x, y = circle.center
    u, v = Vector(x,y)
    circle.center = (x+h*u, y+h*v)

anim = FuncAnimation(figure, animate, frames=60, interval = 70)

plt.show()