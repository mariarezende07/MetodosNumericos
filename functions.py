import numpy as np
from timeit import default_timer as timer
from typing import List, Tuple

def tridigonal_ciclic_matrix(n:int) -> Tuple[np.ndarray, np.ndarray]:
    """ Gera uma sistema linear com uma matriz tridiagonal ciclica

    Args:
        n (int): dimensão da matriz

    Returns:
        Tuple[np.ndarray, np.ndarray]: Matriz A e d do sistema linear
    """
    index = range(1,n+1)
    a = list(map((lambda x : (2*x -1)/(4*x) if x < n else (2*n -1)/(2*n)), index))
    b = [2] * (n)
    c = list(map((lambda x: 1- a[x-1]), index))
    d= list(map((lambda x: np.cos((2 * np.pi * x**2)/n**2)),index))

    A = np.array([a,b,c])
    return A,d

def decompose_LU(A:np.ndarray, n:int)->List[np.ndarray]:
    """Faz a decomposição LU de uma matriz tridiagonal qualquer

    Args:
        A (np.ndarray): Matriz do lado esquerdo do sistema linear
        n (int): Dimensão da matriz

    Returns:
        List[np.ndarray]: Lista com os coeficientes L e U
    """
    u = np.empty(n)
    l = np.empty(n)
    u[0] = A[1][0]
    for i in range(1,n):
        l[i] = (A[0][i]/u[i-1])
        u[i] = A[1][i] - ( l[i] * A[2][i-1] )
    return[l,u]


def tridigonal_system(LU:List[np.ndarray],A:np.ndarray,d:np.ndarray,n:int) -> np.ndarray:
    """Resolve o sistema linear de uma matriz tridiagonal a partir da 
    decomposição LU

    Args:
        LU (List[np.ndarray]): Coeficientes L e U
        A (np.ndarray): Matriz tridiagonal
        d (np.ndarray): Lado direito do sistema linear
        n (int): Dimensão da matriz

    Returns:
        np.ndarray: Array X com a resolução do sistema
    """
    y = np.empty(n)
    y[0] = d[0]    
    for i in range(1,n):
        y[i] = d[i] - LU[0][i]*y[i-1]
    x = np.empty(n)
    x[-1] = y[-1]/LU[1][-1]
    for i in range(n-2, -1 ,-1):
        x[i] = (y[i]-A[2][i]*x[i+1])/LU[1][i]
    return x

def tridigonal_ciclic_system(A:np.ndarray,d:np.ndarray,n:int)->np.ndarray:
    """Resolve o sistema linear de uma matriz tridiagonal cíclica, reaproveitando
    o algoritmo para matrizes tridiagonais simples

    Args:
        A (np.ndarray): Matriz tridiagonal
        d (np.ndarray): Lado direito do sistema linear
        n (int): Dimensão da matriz

    Returns:
        np.ndarray: Array X com a resolução do sistema
    """
    v = np.zeros(n-1)
    v[0] = A[0][0]
    v[-1] = A[2][-2]
    LU = decompose_LU(A, n-1)
    z_til = tridigonal_system(LU, [[0],[0],A[2]], v, n-1)
    y_til = tridigonal_system(LU, [[0],[0],A[2]], d, n-1)
    x = np.empty(n)
    x[-1] = (d[-1] - (A[2][-1]* y_til[0]) - (A[0][-1]*y_til[-1]))/(A[1][-1] -A[2][-1]*z_til[0] - A[0][-1]*z_til[-1]) 
    for i in range(n-2,-1,-1):
        x[i] = y_til[i] - x[-1]*z_til[i] 
    return x
