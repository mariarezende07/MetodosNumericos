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
        l[i] = (vetores[1][i]/u[i-1])
        u[i] = vetores[2][i] - ( l[i] * vetores[3][i-1] )
    return([l,u])

# def tridigonal_system(vetores,n):




# tic = time.perf_counter()
# ciclic_linear_matrix(20)
# toc = time.perf_counter()

# print("meu:",toc-tic)


