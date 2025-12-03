"""                 SOLVEUR EQUATION D4aDVECTION
                        Frédérick MASUAMA
"""
import numpy as np

def solveur_transport(c,nbr_x,x_min,x_max,dt,T,s,ug,ud,p):
    """ Discrétisation"""
    L        = x_max - x_min                                                                           
    h        = L / (nbr_x + 1)
    x        = np.linspace(x_min, x_max, nbr_x + 2)
    M        = int(T / dt)
    lambda_c = c * dt / h

    """vérification CFL"""
    if (lambda_c > 1):
        raise ValueError("La condition de CFL n'est pas respectée", lambda_c)

    """Condition initiale et Conditions aux bords """
    u = np.array([p(xi) for xi in x])
    u[0] = ug
    u[-1] = ud


    """itérations en temps"""
    for j in range(0, M):  
        # Calcul du nouveau u
        u_num = np.copy(u)
        
        if s == 1:   # décentré à gauche
            for i in range(1, nbr_x + 1):
                u_num[i] = u[i] - lambda_c * (u[i] - u[i - 1])
                
        elif s == 2: # décentré à droite
            for i in range(1, nbr_x + 1):
                u_num[i] = u[i] - lambda_c * (u[i + 1] - u[i])
                
        elif s == 3: # Lax-Friedrichs
            for i in range(1, nbr_x + 1):
                u_num[i] = 0.5 * (u[i - 1] + u[i + 1]) - 0.5 * lambda_c * (u[i + 1] - u[i - 1])
        
            # conditions aux bords
        u_num[0] = ug
        u_num[-1] = ud

             # mise à jour
        u = np.copy(u_num)

    """solution exacte"""
    def sol_exacte(x_val):
        return p(x_val- c * T)

    u_exacte = np.array([sol_exacte(xi) for xi in x])

    return x, u, u_exacte


    
