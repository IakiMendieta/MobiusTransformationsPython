import numpy as np

k = 9
q_1 = 3
q_2 = -5

q_pos = np.array([0,0])
q_neg = np.array([4,0])
v = np.array([0,2], dtype=float)

def animate():
    global v
    print("v",v)
    v_ant = v.copy()
    v_1 = v_ant-q_pos
    norma = np.linalg.norm(v_1)
    V_1 = v_1/norma
    v_1 = k*q_1/norma**2*V_1
    print ("v_1",v_1)
    
    v_2 = v_ant-q_neg
    norma = np.linalg.norm(v_2)
    V_2 = v_2/norma
    v_2 = k*q_2/norma**2*V_2
    print("v_2",v_2)

    V=v_1+v_2
    r = np.linalg.norm(V)
    V *= 1/r
    print("V",V)

    v += 0.01*(V)
    print("v",v) 


animate()