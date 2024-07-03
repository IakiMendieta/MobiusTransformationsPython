import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation 

figure, axes = plt.subplots()
circle = plt.Circle((0,1),1)
line = plt.plot([0,0],[0,1], c="r")[0]
axes.add_patch(circle)


#theta'' = -g/l theta

g = 9.81
vth0 = 1 #theta' inicial
th0 = 3 #theta inicial
l = 3 #longitud

def animate(frame):
    global th

    t = 0.1*frame
    w = np.sqrt(g/l)
    th = th0*np.cos(w*t)
    #coordenadas
    x = l*np.sin(th)
    y = -l*np.cos(th)
    #ajustar linea
    line.set_xdata([0,x])
    line.set_ydata([0,y])
    #ajustamos el circulo
    circle.center=(x, y)


anim = FuncAnimation(figure, animate, frames=100, interval = 100)
axes.set_aspect( 1 )

plt.xlim([-4,4])
plt.ylim([-4,3])
plt.show()