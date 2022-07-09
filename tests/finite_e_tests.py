from src.finite_elements import *

def temperatura_barra(L,n, k):

    f = "12*x*(1-x)-2"
    h = L/(n+1)
    x = [(i * h) for i in range(0,n+2)]

    return finite_elements(f, k, n, h, x)

print(temperatura_barra(1,7,"1"))