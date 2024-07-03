import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation 

figure, axes = plt.subplots()
circles = [plt.Circle((0,2*m),1) for m in range(-3,3+1)]
for circle in circles:
    axes.add_patch(circle)


def animate(frame):
    for circle in circles:
        c = circle.get_center()
        circle.center=(0,c[1]+0.1)


anim = FuncAnimation(figure, animate, interval = 60)

axes.set_aspect( 1 )
plt.xlim([-1,1])
plt.ylim([-3,3])
plt.show()