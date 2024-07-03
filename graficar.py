import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation 
import mobiust

i = 0+1j
m = 20

figure, axes = plt.subplots()

circle = plt.Circle( (1,0), 1,  fill = False, color="red")
axes.add_patch(circle)
circle = plt.Circle( (3,0), 3,  fill = False, color="blue" )
axes.add_patch(circle)

T = mobiust.MobT(3,-6,2,0).inverse()

circulos = [plt.Circle((3,0), 3,  fill = False) for _ in range(-m, m)]

for n in range(-m,m) :   
    centro, radio = T.mapCircle(1/2+n*i,1/2)
    x = centro.real
    y = centro.imag
    circulos[n] = plt.Circle( (x,y), radio,  fill = False )
    axes.add_patch(circulos[n])


def animate(frame):
    for n in range(-m,m):
        centro, radio = T.mapCircle(1/2+i*(n+frame*0.1),1/2)
        x = centro.real
        y = centro.imag
        circulos[n].set_radius(radio)
        circulos[n].center = x, y
    return circulos,

"""
for n in range(-10,10) :
    centro, radio = T.mapCircle(1/2+n*i,1/2)
    x = centro.real
    y = centro.imag    
    circle = plt.Circle( (x,y), radio,  fill = False )
    axes.add_patch(circle)
"""

anim = FuncAnimation(figure, func=animate, 
                     frames = 60, interval = 60)
axes.set_aspect( 1 )
plt.xlim([0, 6])
plt.ylim([-3, 3])
plt.title( 'Circle' )
anim.save(filename="girar.gif", writer="pillow")
plt.show()