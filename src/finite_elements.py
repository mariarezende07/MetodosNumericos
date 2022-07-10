import numpy as np
from src.integrals import *
from src.matrixes import *
from src.preprocessing_data import *

def produto_interno(v,w,a,b):
    f_str = "(" +v +")" + "*" + "(" + w + ")"
    return gauss_formula_simple([a,b],f_str,n2)

def funcao_chapeu(h, xf, xb):
    phi_1 = "(x - "+str(xb)+")/"+str(h)
    phi_2 = "("+str(xf) +" - x)/"+ str(h)
    return np.array([phi_1, phi_2])

def finite_elements(f, k, n, h, x):  
    a = []
    b = []
    c = []
    d  = []
    phi_matrix = []
    
    for i in range(1, n+1):
        a.append(-eval(k,{'x':x[i]})/h)
        b.append(2*eval(k,{'x':x[i]})/h)
        c.append(-eval(k,{'x':x[i]})/h)

        phi = funcao_chapeu(h, x[i+1], x[i-1])
        d.append(produto_interno(f,  phi[0],  x[i-1], x[i] ) + produto_interno(f,  phi[1], x[i], x[i+1]))
        phi_matrix.append(eval(phi[0],{'x': x[i]}))
    a[0] = 0
    c[-1] = 0

    
    LU = decompose_LU([a,b,c],n)
    alpha = tridigonal_system(LU,[a,b,c],d,n)

    return np.array(alpha) * np.array(phi_matrix)