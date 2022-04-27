import numpy as np
import math
import time

def tridigonal_ciclic_matrix(n):
    index = range(1,n+1)
    a = list(map((lambda x : (2*x -1)/(4*x) if x <= n - 1 else (2*n -1)/(2*n)), index))
    b = [2] * (n+1)
    c = list(map((lambda x: 1- a[x-1]), index))
    d= list(map((lambda x: np.cos((2 * math.pi * x**2)/n**2)),index))

    return([a,b,c,d])

def decompose_LU(vetores, n):
    u = np.zeros(n)
    l = np.zeros(n)
    u[0] = vetores[2][0]
    for i in range(1,n):
        l[i] = (vetores[0][i]/u[i-1])
        u[i] = vetores[1][i] - ( l[i] * vetores[2][i-1] )
    return([l,u])


def tridigonal_system(LU,vetores,n):
    y = np.empty(n)
    y[0] = vetores[3][0]
    y[1:] = [vetores[3][i] - LU[1][i]*y[i-1] for i in range(1,n)]
    
    x = np.empty(n)
    x[n-1] = y[n-1]/LU[1][n-1]
    x[0:n-2] = [(y[i]-(vetores[2][i]*x[i+1]))/LU[1][i] for i in range(1,n-1)]
    return [x,y]

# def tridigonal_ciclic_system(LU,vetores,n):
    
#     x = np.empty(n)
#     x[n-1] = (vetores[3][n-1] - (vetores[2][n-1]*))()
#     return
tic = time.perf_counter()
vetores = tridigonal_ciclic_matrix(20)
LU = decompose_LU(vetores, 20)
tridigonal_system(LU, vetores, 20)
toc = time.perf_counter()
print("meu:",toc-tic)
# 
# ciclic_linear_matrix(20)
# 

# 


