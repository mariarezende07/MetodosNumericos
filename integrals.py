import numpy as np
import pandas as pd
from preprocessing import n6,n8,n10

def gauss_formula(intervalo,funcao,no):
    n = len(no)
    
    a = intervalo[0]
    b = intervalo[1]
    fc = intervalo[2]
    fd = intervalo[3]
    F = 0
    I = 0

    for i in range(n):
        x_i = no["x_j"][i]
        w_i = no["w_j"][i]
        F = 0
        for j in range(n):
            x_j = no["x_j"][j]
            w_j = no["w_j"][j]
            x = ((b-a)*x_i + a + b)/2            
            d = eval(fd)
            c = eval(fc)
            y = ((d-c)*x_j + c + d)/2            
            F += eval(funcao) * w_j 
        I += F * w_i * (d-c)/2
        
    I *= (b-a)/2
    return I