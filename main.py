import pandas as pd
import numpy as np


from typing import List, Tuple

from src.preprocessing_data import *

from src.matrixes import *
from tests.integrals_tests import *
from tests.matrixes_tests import *
from tests.finite_e_tests import *

def matrixes_mode():
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

def integrals_mode():
    no_atual = 0
    for no in [n6,n8,n10]:
        
        n_str = [6,8,10]
        print(f"""
        Para n = {n_str[no_atual]}:\n
        1) a.Volume do cubo: {volume_cubo(1,no)} \n
           b.Volume do tetraedro: {volume_tetraedro([[0,0,0],[1,0,0],[0,1,0],[0,0,1]],no)}\n
        2) a.Volume  com limite d = 1-x^2: {area_from_curves('1',[0,1,'0','1-(x**2)'],[0,1,'0','np.sqrt(1-y)'],no)[0]}\n
           b.Volume  com limite d = np.sqrt(1-y): {area_from_curves('1',[0,1,'0','1-(x**2)'],[0,1,'0','np.sqrt(1-y)'],no)[1]}\n
        3) a.Area da superfície z=e^(y/x): {superficie([1,-1,1,1],[0.1,0.5,'x**3','x**2'],no)[0]}\n
           b.Volume da superfície z=e^(y/x): {superficie([1,-1,1,1],[0.1,0.5,'x**3','x**2'],no)[1]}\n
        4) a.Volume da calota esférica:{calota(no)}\n
           b.Volume do sólido de revolucao:{volume_solido_rev(no)}\n
        """)
        no_atual+=1

def temperature_mode():
    nums = [7,15,31,63]
    modo = input("1- Gráficos com L = 1 para as diferentes dimensões de N\n\
    2- Erro máximo com L = 1 para as diferentes dimensões de N \n\
    3- Gráficos do equilíbrio com forçantes de calor\n\
    4- Gráficos do equilíbrio com variação de material\n\
    Defina o modo: ")

    if modo == "1":
        questao = input("1- k(x) = 1, q(x) = 0, f(x) = 12*x*(1-x)-2\n\
            2- k(x) = e^x, q(x) = 0, f(x) = e^x + 1")
        if questao == "1":
            grafico_erro(lambda x: (x**2)*(1-x)**2, "1", "12*x*(1-x)-2", 1)
        if questao == "2":
            grafico_erro(lambda x: (x-1)*(np.exp(-x)-1), "np.exp(x)", "np.exp(x) + 1", 1)

    if modo == "2":
        questao = input("1- k(x) = 1, q(x) = 0, f(x) = 12*x*(1-x)-2\n\
        2- k(x) = e^x, q(x) = 0, f(x) = e^x + 1\n")
        if questao == "1":
            for n in nums:
                u_barra = temperatura_barra(1,n, "1", "12*x*(1-x)-2")
                u_x = temperatura_real(lambda x: (x**2)*(1-x)**2, 1, n)
                erro_maximo = erro(u_barra, 1, n, u_x)
                print(f"O erro para N = {n} é: {erro_maximo}")
        if questao == "2":
            for n in nums:
                u_barra = temperatura_barra(1,n, "np.exp(x)", "np.exp(x) + 1")
                u_x = temperatura_real(lambda x: (x-1)*(np.exp(-x)-1), 1, n)
                erro_maximo = erro(u_barra, 1, n, u_x)
                print(f"O erro para N = {n} é: {erro_maximo}")

    if modo == "3":
        Q_n_0 = [100, 100]
        Q_p_0 = [50, 50]
        sigma = [10, 0.1]
        theta = [10, 0.2]
        k = "3.6"
        for i in range(len(Q_n_0)):
            grafico_forcantes_calor_cte(Q_n_0[i],Q_p_0[i],sigma[i], theta[i], k, False)
    if modo == "4":
        Q_n_0 = [100, 100]
        Q_p_0 = [50, 50]
        sigma = [10, 0.1]
        theta = [10, 0.2]
        k = "3.6"
        for i in range(len(Q_n_0)):
            grafico_forcantes_calor_cte(Q_n_0[i],Q_p_0[i],sigma[i], theta[i], k, True)

        

def main():
    """Função principal da aplicação.
    """
    modo = input("1- Matrizes\n2- Integrais\n3- Temperatura num chip\nDefina o modo: ")
    
    if modo == "1":
        matrixes_mode()
    if modo == "2":
        integrals_mode()
    if modo == "3":
        temperature_mode()

if __name__ == "__main__":
    main()

# u_barra = temperatura_barra(1,65,"np.exp(x)","np.exp(x) + 1")
# print(erro(u_barra,1,7, lambda x: (x-1)*(np.exp(-x)-1)))


# u_barra = temperatura_barra(1,7,"1","12*x*(1-x)-2")
# print(erro(u_barra,1,7, lambda x: (x**2)*((1-x)**2)))