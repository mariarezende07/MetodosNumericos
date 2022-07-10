import numpy as np
from src.finite_elements import *
f = "12*x*(1-x)-2"

def temperatura_barra(L,n, k, f):

    
    h = L/(n+1)
    x = [(i * h) for i in range(0,n+2)]
        
    return finite_elements(f, k, n, h, x)

def erro(u_barra, L, n):
    h = L/(n+1)
    x = [(i * h) for i in range(0,n+2)]

    u_x = [(x[i]**2) * ((1-x[i])**2) for i in range(1,n+1)]

    erro = [u_barra[i] - u_x[i] for i in range(n-1)] 

    return np.max(np.absolute(erro)), u_x, u_barra

