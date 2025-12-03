"""
                 DEMANDER A L'UTILISATUER DE DONNER UNE EQUATION 
                              Frédérick MASUAMA
"""

import sympy as sp
import numpy as np
import matplotlib.pyplot as plt


def ecrire_fxt(expr):
    """
    Prend une chaîne 'expression' et retourne une fonction y(x)
    correspondant à cette expression.
    """
    def y(x):
        return eval(expr)
    return y

"""
#Exemple d'usage
t = np.linspace(-1,1,100)
write = input("Entrez u0(x) en Python (ex: 10*(x-0.4) si 0.4<x<0.5): ")
p = ecrire_fxt(write)
#u0_fxt = cond_initiale(t)
        

#plt.plot(t,u0_fxt(t))
plt.plot(t,p(t))
plt.show()
"""

    
    
    
          
