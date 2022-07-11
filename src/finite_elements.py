from typing import List

import numpy as np
from src.integrals import *
from src.matrixes import *
from src.preprocessing_data import *

def produto_interno(v: str,w: str,a:float,b:float) -> float:
    """Realiza o calculo do produto interno entre duas funcoes em um espaco definido

    Args:
        v (str): Primeira funcao
        w (str): Segunda funcao
        a (float): Intervalo "a" de integracao
        b (float): Intervalo "b" de integracao

    Returns:
        float: Valor numerico do calculo do produto interno entre duas funcoes
    """
    f_str = "(" +v +")" + "*" + "(" + w + ")"
    return gauss_formula_simple([a,b],f_str,n2)

def funcao_chapeu(h: float, xf: float, xb: float) -> np.ndarray:
    """_summary_

    Args:
        h (float): Valor do espacamento calculado
        xf (float): Valor de x_i+1
        xb (float): Valor de x_i-1

    Returns:
        np.ndarray: Array contendo os valores de phi no intervalo [x_i-1,x_i] e [x_i,x_i+1] 
    """
    phi_1 = "(x - "+str(xb)+")/"+str(h)
    phi_2 = "("+str(xf) +" - x)/"+ str(h)
    return np.array([phi_1, phi_2])

def finite_elements(f: str, k: str, n: int, h:float, x: List[int]) -> np.ndarray:
    """Faz o calculo da temperatura de uma barra por meio do metodo dos elementos finitos

    Args:
        f (str): funcao f(x) utilizada no calculo do produto interno
        k (str): funcao da condutividade termica do material
        n (int): Dimensao do espaco
        h (float): Valor do espacamento calculado
        x (List[int]): Intervalo da variacao de x entre [0,L]

    Returns:
        np.ndarray: Lista de valores de u_n(x) calculado
    """
    # Instanciamento de listas vazias que terao seu valor definido no loop abaixo
    a = []
    b = []
    c = []
    d  = []
    phi_matrix = []
    
    for i in range(1, n+1):
        # Definicao das diagonais da matriz
        a.append(-eval(k,{'x':x[i],'np':np,'L':1,'d':-1})/h)
        b.append(2*eval(k,{'x':x[i],'np':np,'L':1,'d':-1})/h)
        c.append(-eval(k,{'x':x[i],'np':np,'L':1,'d':-1})/h)
        # Cálculo da funcao chapeu de phi
        phi = funcao_chapeu(h, x[i+1], x[i-1])
        # Calculo dos produtos internos que definem o lado direito do sistema
        d.append(produto_interno(f,  phi[0],  x[i-1], x[i] ) + produto_interno(f,  phi[1], x[i], x[i+1]))
        # Armazenamento dos valores de phi no intervalo [x_i-1,x_i]
        phi_matrix.append(eval(phi[0],{'x': x[i]}))
    # Correção dos valores para matrizes tridiagonais
    a[0] = 0
    c[-1] = 0
    # Decomposicao LU da matriz tridiagonal gerada
    LU = decompose_LU([a,b,c],n)
    # Resolucao do sistema
    alpha = tridigonal_system(LU,[a,b,c],d,n)
    
    return np.array(alpha) * np.array(phi_matrix)