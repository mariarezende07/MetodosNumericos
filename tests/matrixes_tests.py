import matplotlib.pyplot as plt
from numpy import ndarray
from timeit import default_timer as timer
from typing import List, Tuple
from src.matrixes import tridigonal_ciclic_matrix, tridigonal_ciclic_system

def matrix_from_dimension(n:int)-> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Calcula um sistema tridiagonal cíclico a partir da dimensão dele

    Args:
        n (int): Dimensão da matriz do sistema

    Returns:
        Tuple[np.ndarray, np.ndarray, np.ndarray]: Retorna 3 arrays, sendo elas a matriz do sistema, o lado
        direito do sistema e as soluções
    """
    A,d = tridigonal_ciclic_matrix(n)
    x = tridigonal_ciclic_system(A,d, n)
    return A, d, x

def time_taken(inicio:int,fim:int,step:int) -> None:
    """Calcula o tempo tomado para calcular a solução de um sistema tridiagonal cíclico dado um intervalo
    e plota um gráfico

    Args:
        inicio (int): Início do intervalo
        fim (int): Fim do intervalo
        step (int): Steps do intervalo
    """
    x = list(range(inicio,fim,step))
    tempos = []
    for n in range(inicio,fim,step):
        start = timer()
        matrix_from_dimension(n)
        end = timer()
        tempos.append(end-start)
    plt.plot(x,tempos)
    plt.show()

