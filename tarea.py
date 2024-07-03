import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation 

figure, axes = plt.subplots()


#axes.ylim=(-4,4)

circle = plt.Circle((-0.5,-0.5),0.1)
axes.add_patch(circle)

x = lambda t: np.sin(2*t)
y = lambda t: np.cos(3*t)

def animate(frame):
    h = 0.03
    t = h*frame
    circle.center = (x(t), y(t))

anim = FuncAnimation(figure, animate, frames=200, interval = 70)


axes.set_xlim(-3,3)
axes.set_ylim(-3,3)
plt.show()