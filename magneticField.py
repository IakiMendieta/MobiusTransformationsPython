#Importamos las bibliotecas
import matplotlib.pyplot as plt
import numpy as np
#Para crear la animación
from matplotlib.animation import FuncAnimation 

#Obtenemos la figura y el axes
figure, axes = plt.subplots()
#Parametos para la simulación
k = 9
q_1 = 2 #Intensidad de la carga positiva
q_2 = -1 #Intensidad de la carga negativa
#Tomaremos puntos al rededor de la carga positiva.
r = 0.32 #Radio al rededor de donde tomamos puntos
n = 150 #Número de puntos al rededor
#Posiciones
q_pos = np.array([0,0]) #Carga positiva
q_neg = np.array([3,0]) #Carga negativa
vectores = [np.array([r*np.cos(t)+q_pos[0], r*np.sin(t)+q_pos[1]]) 
            for t in np.linspace(-np.pi, 
                                 np.pi,n)] #Los puntos al rededor de la carga postiva
x_datas = [[v[0]] for v in vectores] #posiciones x de estos puntos
y_datas = [[v[1]] for v in vectores] #posiciones y de estos puntos
lineas = [axes.plot([],[], c='black')[0] for _ in vectores] #Linea de la posicion de cada punto
#Bolitas de carga positiva y negativa
pos = plt.Circle((q_pos[0],q_pos[1]),0.2,color='red')
neg = plt.Circle((q_neg[0],q_neg[1]),0.2,color='blue')
#Los ponemos en pantalla
axes.add_patch(pos)
axes.add_patch(neg)
#Etiquetas de +/-
axes.annotate("+", xy=(q_pos[0],q_pos[1]),fontsize=20,ha='center',va='center')
axes.annotate("—", xy=(q_neg[0],q_neg[1]),fontsize=20,ha='center',va='center',color='white')
#Limites de visulización
axes.set_xlim(-0.3, 3.3)
axes.set_ylim(-2,2)
axes.set_aspect('equal')
#Función de animación
def animate(frame):
    global vectores
    #Actualizaremos la posición de cada punto
    for i,v in enumerate(vectores):
        #Componente hacia la carga postiva
        v_1 = v-q_pos
        norma = np.linalg.norm(v_1)
        V_1 = v_1/norma
        v_1 = k*q_1/norma**2*V_1
        #Componente hacia la carga negativa
        v_2 = v-q_neg
        norma = np.linalg.norm(v_2)
        V_2 = v_2/norma
        v_2 = k*q_2/norma**2*V_2
        #Sumamos y normalizamos
        V=v_1+v_2
        r = np.linalg.norm(V)
        V *= 1/r
        #Si no estamos muy lejos ni muy cerca de la carga negativa
        if np.linalg.norm(v-q_neg)>0.3:
            #Nos movemos un poco hacia allá
            v += 0.06*(V)
            #Actualizamos la posición
            x_datas[i].append(v[0])
            y_datas[i].append(v[1])
            lineas[i].set_data(x_datas[i],y_datas[i])
#Animar y mostrar.
anim= FuncAnimation(figure, animate, frames=200, interval=10,repeat=False)
axes.set_title("Campo magnético dos cargas.")
plt.show()