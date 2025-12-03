import numpy as np
import matplotlib.pyplot as plt
from solveur import*


"""erreur = abs(u_num - sol_exacte_val)
print("err est:",max(erreur))"""


"""condition initiale"""
def u0(x):
    return np.exp(-100*(x-0.5)**2)

"""paramètres"""
c = 1
nx = 200
xmin, xmax = 0, 1
T = 0.4
ug, ud = float(input())
s = 1
"""valeurs à essayer"""
CFL_val = [0.5, 1.0, 1.2]


"""tests des valeurs de CFL"""
for CFL in CFL_val:
    dx = (xmax - xmin) / nx
    dt = CFL * dx / c

    solver = solveur_transport(c, nx, xmin, xmax, dt,T,s,ug,ud,p)
    u_final = solver.run(u0, T)

    plt.plot(solver.x, u_final, label=f"CFL = {CFL}")

plt.legend()
plt.title("Influence de la condition CFL sur la stabilité de l’Upwind")
plt.show()
