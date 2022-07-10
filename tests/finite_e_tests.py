import numpy as np
from src.finite_elements import *
import matplotlib.pyplot as plt

def temperatura_barra(L,n, k, f):

    
    h = L/(n+1)
    x = [(i * h) for i in range(0,n+2)]
        
    return finite_elements(f, k, n, h, x)

def erro(u_barra, L, n, f):
    h = L/(n+1)
    x = [(i * h) for i in range(0,n+2)]

    u_x = [f(x[i]) for i in range(1,n+1)]

    erro = [u_barra[i] - u_x[i] for i in range(n-1)] 

    return np.max(np.absolute(erro)), u_x

def plotting_calc_error(u_barra, u_x, x):
    plt.style.use('_mpl-gallery')
    fig, ax = plt.subplots()

    ax.plot(x, u_barra, linewidth=2.0)

    plt.show()

# u_barra = temperatura_barra(1,63,"np.exp(x)","np.exp(x) + 1")
# n=63
# u_x = erro(u_barra,1,63, lambda x: (x-1)*(np.exp(-x)-1))[1]
# L = 1
# h = L/(n+1)

# x = [(i * h) for i in range(1,n+1)]
# plotting_calc_error(u_barra, u_x, x)

