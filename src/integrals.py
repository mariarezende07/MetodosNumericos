from typing import List, Tuple
import pandas as pd
import numpy as np
from src.preprocessing_data import *

def gauss_formula(intervalo:List,funcao:str,no:pd.DataFrame) -> float:
    """Aplica a formula de gauss para resolver uma integral dupla dado um determinado intervalo

    Args:
        intervalo (List[int,int,str,str]): Lista com os valores dos intervalos a,b,c,d , sendo a e b inteiros
        e c e d strings
        funcao (str): String representando a funcao
        no (pd.DataFrame): Tabela dos nós e seus respectivos pesos

    Returns:
        float: Valor numérico da integração
    """
    # Determina o tamanho da lista de nós que estamos trabalhando e os intervalos
    n = len(no)    
    a = intervalo[0]
    b = intervalo[1]
    fc = intervalo[2]
    fd = intervalo[3]

    F = 0
    I = 0
    # Realiza as duas somatórias necessárias
    for i in range(n):
        x_i = no["x_j"][i]
        w_i = no["w_j"][i]
        F = 0
        for j in range(n):
            x_j = no["x_j"][j]
            w_j = no["w_j"][j]
            # Ajusta X e Y no intervalo dado
            x = ((b-a)*x_i + a + b)/2            
            d = eval(fd) # Dada a função d, calcula o valor com o resultado obtido acima de X
            c = eval(fc) # Dada a função c, calcula o valor com o resultado obtido acima de X
            y = ((d-c)*x_j + c + d)/2            
            F += eval(funcao) * w_j  # Dada a função f(x,y), calcula os valores com os resultados obtidos e pelo peso
        # Multiplica a função F por uma constante para ajustar o valor no intervalo dado
        I += F * w_i * (d-c)/2
    # Multiplica a integral I por uma constante para ajustar o valor no intervalo dado
    I *= (b-a)/2
    return I

def gauss_formula_simple(intervalo:List,funcao:str,no:pd.DataFrame) -> float:
    """Aplica a formula de gauss para resolver uma integral simples dado um determinado intervalo

    Args:
        intervalo (List[int,int]): Lista com os valores dos intervalos a,b
        funcao (str): String representando a funcao
        no (pd.DataFrame): Tabela dos nós e seus respectivos pesos

    Returns:
        float: Valor numérico da integração
    """
    # Determina o tamanho da lista de nós que estamos trabalhando e os intervalos
    n = len(no)    
    a = intervalo[0]
    b = intervalo[1]

    F = 0
    # Realiza as duas somatórias necessárias
    for i in range(n):
        x_i = no["x_j"][i]
        w_i = no["w_j"][i]
        # Ajusta X e Y no intervalo dado
        x = ((b-a)*x_i + a + b)/2     
        F += eval(funcao) * w_i  # Dada a função f(x,y), calcula os valores com os resultados obtidos e pelo peso
        
    # Multiplica a integral I por uma constante para ajustar o valor no intervalo dado
    F *= (b-a)/2
    return F
