from typing import Callable
import numpy as np
from src.finite_elements import *
from plotly.subplots import make_subplots
import plotly.graph_objects as go

def temperatura_barra(L: float,n: int, k: str, f: str) -> np.ndarray:
    """Calcula a temperatura aproximada da barra pelo método de elementos finitos

    Args:
        L (float): Comprimento da barra
        n (int): Dimensao do espaco
        k (str): Condutividade termica do material
        f (str): Funcao da variacao de calor na barra

    Returns:
        np.ndarray: Lista de valores de u_n(x) calculado
    """
    h = L/(n+1)
    x = [(i * h) for i in range(0,n+2)]
        
    return finite_elements(f, k, n, h, x)


def temperatura_real(f_u: Callable, L: float, n:int) -> List[float]:
    """Calcula a temperatura da barra por meio de uma equacao dada

    Args:
        f_u (Callable): Funcao da variacao de calor na barra
        L (float): Comprimento da barra
        n (int): Dimensao do espaco

    Returns:
        List[float]: Lista de valores de u(x)
    """
    h = L/(n+1)
    x = [(i * h) for i in range(0,n+2)]
    u_x = [f_u(x[i]) for i in range(1,n+1)]
    return u_x

#print(temperatura_barra(1,7,"3.6 if(x >= L/2 - d and  x <= L/2 + d) else 60","np.exp(x) + 1"))

def erro(u_barra, L, n, u_x):
    h = L/(n+1)
    x = [(i * h) for i in range(0,n+2)]
    erro = np.subtract(u_x,u_barra)
    erro_max = np.max(np.abs(erro))
    return erro_max

def grafico_erro(f_u: Callable, k: str, f_u_barra: str, L: float) -> None:
    """Funcao que gera um subplot com as funcoes calculadas nos espacos definidos pelo exercicio

    Args:
        f_u (Callable): Funcao que calcula u(x)
        k (str): Condutividade termica do material
        f_u_barra (str): Funcao da variacao de calor na barra
        L (float): Comprimento da barra
    """
    fig = make_subplots(rows=1, cols=4, subplot_titles=("N = 7", "N = 15", "N = 31", "N = 63"))
    nums = [7,15,31,63]
    # Percorre os espacos definidos
    for i in range(len(nums)):
        n = nums[i]
        # Calcula a temperatura por meio do método dos elementos finitos e pela funcao resposta dada
        u_x = temperatura_real(f_u, L, n)
        u_barra = temperatura_barra(L,n,k,f_u_barra)
        # Definicao das constantes
        
        h = L/(n+1)
        x = [(i * h) for i in range(1,n+1)]
        # Calculo da array do erro
        error= np.subtract(u_x,u_barra)

        # Plotando por meio do Plotly
        fig.add_trace(go.Scatter(
            x= x,
            y= np.array(u_barra),
            mode='lines+markers',
            name='un(x)',
            error_y=dict(
                type='data',
                array= error,
                symmetric=False)
            ),            
            row=1, col=1+i)
        fig.add_trace(go.Scatter(
        x= x,
        y= np.array(u_x),
        mode='lines+markers',
        name='u(x)'
        ),
        row=1, col=1+i)
    fig.update_layout(title='Temperatura calculada por funcao resposta e metodo dos elementos finitos',
                   height=600, width=1400)
    fig.show()

def curva_prevista(x,u_barra):
    return np.poly1d(np.polyfit(x,u_barra, 2))

def forcantes_calor(Q_n_0: float,Q_p_0: float,sigma: float, theta: float, k: str, n: int) -> List[float]:
    """Calcula a variacao da temperatura levando em conta o calor que entra e sai

    Args:
        Q_n_0 (float): Constante de resfriamento
        Q_p_0 (float): Maximo calor gerado no centro do chip
        sigma (float): Variacao da geracao de calor
        theta (float): Constante da variacao do calor
        k (str): Condutividade termica do material
        n (int): Dimensao do espaco

    Returns:
        List[float]: Lista de valores de u_n(x) calculado
    """
    L = 1

    Q_plus = str(Q_p_0) + "*np.exp( -( (x-"+str(L)+")/2 )**2 )/("+str(sigma)+"**2))"
    Q_minus = str(Q_n_0) + "*( np.exp(-((x)**2) /("+str(theta)+"**2))+np.exp(-((x-"+str(L)+")**2)/("+str(theta)+"**2)))"
    
    Q = "(" +Q_plus + ") - (" + Q_minus + ")"
    
    return temperatura_barra(L,n, k, Q)

def grafico_forcantes_calor_cte(Q_n_0,Q_p_0,sigma, theta, k):
    fig = make_subplots(rows=1, cols=4, subplot_titles=("N = 7", "N = 15", "N = 31", "N = 63"))
    nums = [7,15,31,63]
    for i in range(len(nums)):
        n = nums[i]
        u_barra = forcantes_calor(Q_n_0,Q_p_0,sigma, theta, k, n)
        L = 1
        h = L/(n+1)
        x = [(i * h) for i in range(1,n+1)]
        fig.add_trace(go.Scatter(
            x= x,
            y= np.array(u_barra),
            mode='lines+markers',
            name='un(x)'),      
            row=1, col=1+i)
    fig.update_layout(title="Temperatura calculada levando em conta parâmetros variáveis\nQ_0+ ="+str(Q_p_0)+"Q_0- = "+str(Q_p_0)+"\nsigma ="+str(sigma)+"theta = "+str(theta),
                   xaxis_title='Espaçamento',
                   yaxis_title='Temperatura da barra',
                   height=600, width=1400)
    fig.show()
