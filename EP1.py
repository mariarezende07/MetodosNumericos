import numpy as np
import math
import time

def tridigonal_ciclic_matrix(n):
    index = range(1,n+1)
    a = list(map((lambda x : (2*x -1)/(4*x) if x <= n - 1 else (2*n -1)/(2*n)), index))
    b = [2] * (n)
    c = list(map((lambda x: 1- a[x-1]), index))
    d= list(map((lambda x: np.cos((2 * math.pi * x**2)/n**2)),index))

    A = np.array([a,b,c])
    return(A,d)

def decompose_LU(A, n):
    u = np.empty(n)
    l = np.empty(n)
    u[0] = A[2][0]
    for i in range(1,n):
        l[i] = (A[0][i]/u[i-1])
        u[i] = A[1][i] - ( l[i] * A[2][i-1] )
    return([l,u])


def tridigonal_system(LU,A,d,n):
    y = np.empty(n)
    y[0] = d[0]
    y[1:] = [d[i] - LU[1][i]*y[i-1] for i in range(1,n)]
    
    x = np.empty(n)
    x[n-1] = y[n-1]/LU[1][n-1]
    x[0:n-2] = [(y[i]-(A[2][i]*x[i+1]))/LU[1][i] for i in range(1,n-1)]
    return x

def tridigonal_ciclic_system(LU,A,d,n):
    v = np.zeros(n)
    w = np.zeros(n)

    v[0] = A[0][0]
    v[n-1] = A[2][n-2]

    w[0] = A[2][n-1]
    w[n-1] = A[0][n-1]

    z_til = tridigonal_system(LU, [0,0,A[2]], v, n-1)
    y_til = tridigonal_system(LU, [0,0,A[2]], d, n-1)

    x = np.empty(n)
    x[n-1] = (d[n-1] - (A[2][n-1]* y_til[0]) - (A[0][n-1]*y_til[n-2]))/(A[1][n-1] - (A[2][n-2]*z_til[0]) - (A[0][n-1]*z_til[n-2])) 
    x[0:n-2] = [y_til[i] - (x[n-1]*z_til[i]) for i in range(1,n-1)]

    return x
tic = time.perf_counter()
A,d = tridigonal_ciclic_matrix(20)
LU = decompose_LU(A, 20)
tridigonal_ciclic_system(LU, A,d, 20)
toc = time.perf_counter()
print("meu:",toc-tic)
# 
# ciclic_linear_matrix(20)
# 

# 


