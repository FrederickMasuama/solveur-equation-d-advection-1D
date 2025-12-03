"""                    EXEMPLES D'APPLICATION
                        MASUAMLA Frédérick
"""

import numpy as np
from solveur import solveur_transport
from redac_fxt_utilisateur import ecrire_fxt

"=============================================================================="
def pulse_gaussien(x):
    return np.exp(-50*(x-0.3)**2)

def onde_carree(x):
    return np.where((x>=0.2) & (x<=0.4),1.0, 0.0)

def onde_sinusoidale(x):
    return np.sin(2*np.pi*x)

"=============================================================================="

print("Rentrez 1 pour la pulsion gaussienne, 2 pour l'onde carrée, 3 pour l'onde sinusoïdale et 4 pour donner une fonction")
choix = int(input("votre choix est :"))


if (choix == 1):
    p = pulse_gaussien
elif (choix == 2):
    p = onde_carree
elif(choix == 3):
    p = onde_sinusoidale
elif(choix == 4):
    write = input("Entrez u0(x) en Python (ex: 10*(x-0.4) si 0.4<x<0.5): ")
    p = ecrire_fxt(write)
else:    
    raise ValueError("Valeur invalide")
"=============================================================================="

""" Paramètres utilisateur """
c     = float(input("Vitesse c = "))
nbr_x = int(input("Nombre de points intérieurs N = "))
x_min = float(input("x_min = "))
x_max = float(input("x_max = "))
dt    = float(input("Pas de temps dt = "))
T     = float(input("Temps final T = "))
s     = int(input("Schéma (1=gauche, 2=droite, 3=Lax-Friedrichs) = "))
ug    = float(input("Condition bord gauche = "))
ud    = float(input("Condition bord droit = "))

""" Lancement du solveur """
x, u_num, u_exacte = solveur_transport(c, nbr_x, x_min, x_max, dt, T, s, ug, ud, p)

""" Affichage """
#trace_solution(x, u_num, u_exacte, p)

#print("Erreur max =", np.max(np.abs(u_num - u_exacte)))

