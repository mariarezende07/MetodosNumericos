from typing import List, Tuple
import pandas as pd
import numpy as np
from src.integrals import *

def volume_cubo(aresta: float, nos:pd.DataFrame) -> float:
    """Calcula o volume de um cubo dado o tamanho de uma aresta com integrais duplas

    Args:
        aresta (float): Tamanho da aresta do cubo
        nos (pd.DataFrame): Tabela dos nós e seus respectivos pesos

    Returns:
        float: Volume do cubo
    """
    volume = gauss_formula([0,aresta,"0",str(aresta)],"1", nos)
    return volume

def volume_tetraedro(vertices:List, nos:pd.DataFrame) -> float:
    """Calcula a equação de variação de Y e a equação do plano dados 4 vértices
    para calcular o volume de um tetraedro qualquer a partir de integrais duplas

    Args:
        vertices (List): Vertices do tetraedro
        nos (pd.DataFrame): Tabela dos nós e seus respectivos pesos

    Returns:
        float: Volume do tetraedro
    """
    v_1 = np.subtract(vertices[2],vertices[1])
    v_2 = np.subtract(vertices[3],vertices[1])
    n = np.cross(v_1,v_2)
    d = np.dot(n,vertices[1]) 
    
    eq_plano = "("+ str(n[0]) + "* x +" + str(n[1]) + "* y -(" + str(d) + "))/"+ str(-n[2])
    
    y_var = str(d) + "-" + str(vertices[1][0]) + "* x"
    volume = gauss_formula([0,vertices[1][0],str(vertices[0][1]),str(y_var)],eq_plano, nos)
    return volume

def area_from_curves(curva: str, limites_1:List, limites_2:List, nos:pd.DataFrame)->Tuple[float,float]:
    """A partir de uma curva, calcula o volume de duas formas diferentes

    Args:
        curva (str): Equação da curva
        limites_1 (List): Limite 1 a ser testado
        limites_2 (List): Limite 2 a ser testado
        nos (pd.DataFrame): Tabela dos nós e seus respectivos pesos

    Returns:
        Tuple[float,float]: Tupla com o volume calculado da primeira e da segunda forma
    """
    volume_1 = gauss_formula(limites_1,curva,nos)
    limites_2[3] = limites_2[3].replace("y", "x")
    volume_2 = gauss_formula(limites_2,curva,nos)
    return volume_1, volume_2

def superficie(plano:List, limites:List, nos:pd.DataFrame) -> Tuple[float,float]:
    """A partir de uma equação de superficie expoencial, calcula a equação da area como dado pelo exemplo.
    Então, integra a area e a superficie nos limites dados para achar a area e o volume

    Args:
        plano (List): Recebe a seguinte lista com os multiplicadores e expoentes de x e y: [mx,ex,my,ey]
        limites (List): Limites dados para calcular as integrais duplas        
        nos (pd.DataFrame): Tabela dos nós e seus respectivos pesos

    Returns:
        Tuple[float,float]: Area e volume da superfície
    """

    exponent = str(plano[0]) + "* (x**"+str(plano[1])+")*"+str(plano[2]) + "* (y**"+str(plano[3])+")"
    partial_x = str(plano[0]) + "*" +str(plano[1]) + "*(x**" + str(plano[1] - 1) +")* (y**"+str(plano[3]) +")*" + str(plano[2])
    partial_y = str(plano[2]) + "*" +str(plano[3]) + "*(y**" + str(plano[3] - 1) +")* (x**"+str(plano[1]) +")*" + str(plano[0])
    
    area_equation = "np.sqrt(("+partial_x+"*np.exp("+exponent+"))**2 + (("+partial_y+"*np.exp("+exponent+"))**2 + 1))"
    
    area = gauss_formula(limites, area_equation, nos)
    volume = gauss_formula(limites, "np.exp("+exponent+")", nos)
    return area, volume
    
def calota(nos:pd.DataFrame) -> float:
    """Calcula o volume da calota formada pela equação do exemplo 4

    Args:
        nos (pd.DataFrame): Tabela dos nós e seus respectivos pesos

    Returns:
        float: Volume da calota
    """
    return 2 * np.pi * gauss_formula([3/4,1,'0','np.sqrt(1 -(x**2))'], 'y' , nos)


def volume_solido_rev(nos:pd.DataFrame) -> float:
    """Calcula o volume do sólido de revolução dado pelo exemplo 4

    Args:        
        nos (pd.DataFrame): Tabela dos nós e seus respectivos pesos

    Returns:
        float: Volume do sólido de revolução
    """
    return 2 * np.pi * gauss_formula([-1,1,'0','np.exp(-x**2)'], 'y', nos)