import numpy as np
from integrals import *
from matrixes import *
from preprocessing_data import *

def produto_interno(v,w,a,b):
    f_str = "(" +v +")" + "*" + "(" + w + ")"
    return gauss_formula_simple([a,b],f_str,n10)

def funcao_chapeu(h, xf, xb):
    phi_1 = "(x - "+str(xb)+")/"+str(h)
    phi_2 = "("+str(xf) +" - x)/"+ str(h)

    return np.array([phi_1, phi_2])

def base_splines(k,h,n):
    a  = [-eval(k)/h for i in range(n)]
    b = [2*eval(k)/h for i in range(n)]
    c = [-eval(k)/h for i in range(n)]
    return [a,b,c]



def finite_elements(f, k, n, h, x):     
    A = base_splines(k,h,n)
    d  = []
    phi_matrix = []

    for i in range(1, n+1):
        phi = funcao_chapeu(h, x[i+1], x[i-1])
        d.append(produto_interno(f,  phi[0],  x[i-1], x[i] ) + produto_interno(f,  phi[1], x[i], x[i+1]))
        phi_matrix.append(eval(phi[0],{'x': x[i]}))

    LU = decompose_LU(A,n)
    alpha = tridigonal_system(LU,A,d,n)

    return np.array(alpha) * np.array(phi_matrix)

def erro(u_barra, h, x, n):
    u_x = []
    for i in range(n):
        u_x.append((x[i]**2) * ((1-x[i])**2))

    erro = np.array([])
    for i in range(n-1):

        erro = np.append(erro, u_barra[i] - u_x[i])

    return np.max(np.absolute(erro))

def temperatura_barra(L,n, k):

    f = "12*x*(1-x)-2"
    h = L/(n+1)
    x = [(i * h) for i in range(0,n+2)]

    return finite_elements(f, k, n, h, x)

print(temperatura_barra(1,7,"1"))
    







