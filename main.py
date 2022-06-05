import pandas as pd
import numpy as np

from typing import List, Tuple

from src.preprocessing_data import *
from src.integrals import *
from src.matrixes import *
from tests.integrals_tests import *
from tests.matrixes_tests import *

def main():
    """Função principal da aplicação.
    """
    modo = input("1- Matriz por dimensão\n2- Verificar tempo do algoritmo\nDefina o modo: ")

    if modo == "1":
        n = int(input("Digite a dimensão da matriz: "))
        A, d, x = matrix_from_dimension(n)

        x_str = ["x_"+ str(i) for i in range(1,n+1)]
        print(f"A matriz A consiste em:\na = {A[0]}\nb={A[1]}\nc={A[2]}\n")
        print(f"O vetor d consiste em:\nd={d}\n")

        solucoes = np.array([ x_str[i] + " = " + str(x[i]) for i in range(n)]).reshape(n,1)
        
        print(f"As soluções são:{solucoes}")
    
    if modo =="2":
        inicio = int(input("Insira o início do intervalo: "))
        fim = int(input("Insira o fim do intervalo: "))
        step = int(input("Insira o step do intervalo: "))

        time_taken(inicio,fim,step)

if __name__ == "__main__":
    main()

