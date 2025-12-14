import numpy as np
import matplotlib.pyplot as plt
from solveur import *


# --- condition initiale ---
def u0(x):
    return np.exp(-100 * (x - 0.5)**2)

# --- paramètres ---
c = 1
nx = 200
xmin, xmax = 0, 2
T = 0.4
ug = float(input("Bord gauche = "))
ud = float(input("Bord droit = "))
s = 1

# --- liste des CFL ---
CFL_val = [0.5, 0.8, 1.0, 1.2]

for CFL in CFL_val:

    dx = (xmax - xmin) / nx
    dt = CFL * dx / c

    # solveur
    x, u_final, u_exacte = solveur_transport(
        c, nx, xmin, xmax, dt, T, s, ug, ud, u0
    )

    plt.plot(x, u_final, label=f"CFL = {CFL}")

plt.plot(x, u0(x), label="sol init")
plt.legend()
plt.title("Influence de la CFL sur la stabilité du schéma Upwind")
plt.xlabel("x")
plt.ylabel("u")
plt.show()
