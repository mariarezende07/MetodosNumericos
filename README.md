<h1 align="center">
    🔢 Exercício programa de Métodos Numéricos
</h1>

<div style="text-align:center">

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)
[![forthebadge](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNTEuOTMiIGhlaWdodD0iMzUiIHZpZXdCb3g9IjAgMCAxNTEuOTMgMzUiPjxyZWN0IGNsYXNzPSJzdmdfX3JlY3QiIHg9IjAiIHk9IjAiIHdpZHRoPSI4MC45OSIgaGVpZ2h0PSIzNSIgZmlsbD0iI0VBNDU2MCIvPjxyZWN0IGNsYXNzPSJzdmdfX3JlY3QiIHg9Ijc4Ljk5IiB5PSIwIiB3aWR0aD0iNzIuOTQiIGhlaWdodD0iMzUiIGZpbGw9IiNDMTNCM0EiLz48cGF0aCBjbGFzcz0ic3ZnX190ZXh0IiBkPSJNMTkuNTcgMjJMMTQuMjIgMjJMMTQuMjIgMTMuNDdMMTUuNzAgMTMuNDdMMTUuNzAgMjAuODJMMTkuNTcgMjAuODJMMTkuNTcgMjJaTTIzLjQzIDE4LjAwTDIzLjQzIDE4LjAwTDIzLjQzIDE3LjUyUTIzLjQzIDE2LjI4IDIzLjg3IDE1LjMyUTI0LjMxIDE0LjM3IDI1LjEyIDEzLjg2UTI1LjkyIDEzLjM1IDI2Ljk3IDEzLjM1UTI4LjAxIDEzLjM1IDI4LjgyIDEzLjg1UTI5LjYyIDE0LjM1IDMwLjA2IDE1LjI5UTMwLjUwIDE2LjIzIDMwLjUxIDE3LjQ4TDMwLjUxIDE3LjQ4TDMwLjUxIDE3Ljk2UTMwLjUxIDE5LjIxIDMwLjA3IDIwLjE2UTI5LjY0IDIxLjEwIDI4LjgzIDIxLjYxUTI4LjAzIDIyLjEyIDI2Ljk4IDIyLjEyTDI2Ljk4IDIyLjEyUTI1Ljk0IDIyLjEyIDI1LjEzIDIxLjYxUTI0LjMyIDIxLjEwIDIzLjg4IDIwLjE3UTIzLjQzIDE5LjIzIDIzLjQzIDE4LjAwWk0yNC45MSAxNy40NkwyNC45MSAxNy45NlEyNC45MSAxOS4zNiAyNS40NiAyMC4xM1EyNi4wMSAyMC45MCAyNi45OCAyMC45MEwyNi45OCAyMC45MFEyNy45NiAyMC45MCAyOC40OSAyMC4xNVEyOS4wMiAxOS40MCAyOS4wMiAxNy45NkwyOS4wMiAxNy45NkwyOS4wMiAxNy41MVEyOS4wMiAxNi4wOSAyOC40OSAxNS4zNFEyNy45NSAxNC41OCAyNi45NyAxNC41OEwyNi45NyAxNC41OFEyNi4wMSAxNC41OCAyNS40NiAxNS4zM1EyNC45MiAxNi4wOSAyNC45MSAxNy40NkwyNC45MSAxNy40NlpNMzYuNjUgMTQuNjZMMzQuMDIgMTQuNjZMMzQuMDIgMTMuNDdMNDAuNzggMTMuNDdMNDAuNzggMTQuNjZMMzguMTIgMTQuNjZMMzguMTIgMjJMMzYuNjUgMjJMMzYuNjUgMTQuNjZaTTUwLjI1IDE4LjAwTDUwLjI1IDE4LjAwTDUwLjI1IDE3LjUyUTUwLjI1IDE2LjI4IDUwLjY5IDE1LjMyUTUxLjEzIDE0LjM3IDUxLjk0IDEzLjg2UTUyLjc0IDEzLjM1IDUzLjc5IDEzLjM1UTU0LjgzIDEzLjM1IDU1LjYzIDEzLjg1UTU2LjQ0IDE0LjM1IDU2Ljg4IDE1LjI5UTU3LjMyIDE2LjIzIDU3LjMyIDE3LjQ4TDU3LjMyIDE3LjQ4TDU3LjMyIDE3Ljk2UTU3LjMyIDE5LjIxIDU2Ljg5IDIwLjE2UTU2LjQ2IDIxLjEwIDU1LjY1IDIxLjYxUTU0Ljg1IDIyLjEyIDUzLjgwIDIyLjEyTDUzLjgwIDIyLjEyUTUyLjc2IDIyLjEyIDUxLjk1IDIxLjYxUTUxLjE0IDIxLjEwIDUwLjY5IDIwLjE3UTUwLjI1IDE5LjIzIDUwLjI1IDE4LjAwWk01MS43MyAxNy40Nkw1MS43MyAxNy45NlE1MS43MyAxOS4zNiA1Mi4yOCAyMC4xM1E1Mi44MiAyMC45MCA1My44MCAyMC45MEw1My44MCAyMC45MFE1NC43OCAyMC45MCA1NS4zMSAyMC4xNVE1NS44NCAxOS40MCA1NS44NCAxNy45Nkw1NS44NCAxNy45Nkw1NS44NCAxNy41MVE1NS44NCAxNi4wOSA1NS4zMSAxNS4zNFE1NC43NyAxNC41OCA1My43OSAxNC41OEw1My43OSAxNC41OFE1Mi44MiAxNC41OCA1Mi4yOCAxNS4zM1E1MS43NCAxNi4wOSA1MS43MyAxNy40Nkw1MS43MyAxNy40NlpNNjMuMjcgMjJMNjEuNzkgMjJMNjEuNzkgMTMuNDdMNjcuMjEgMTMuNDdMNjcuMjEgMTQuNjZMNjMuMjcgMTQuNjZMNjMuMjcgMTcuMjBMNjYuNzEgMTcuMjBMNjYuNzEgMTguMzhMNjMuMjcgMTguMzhMNjMuMjcgMjJaIiBmaWxsPSIjRkZGRkZGIi8+PHBhdGggY2xhc3M9InN2Z19fdGV4dCIgZD0iTTk1LjM4IDIyTDkzLjE4IDIyTDkzLjE4IDEzLjYwTDk1LjEzIDEzLjYwTDk4LjA5IDE4LjQ1TDEwMC45NyAxMy42MEwxMDIuOTIgMTMuNjBMMTAyLjk1IDIyTDEwMC43NyAyMkwxMDAuNzQgMTcuNTVMOTguNTggMjEuMTdMOTcuNTMgMjEuMTdMOTUuMzggMTcuNjdMOTUuMzggMjJaTTEwOS41MyAyMkwxMDcuMTAgMjJMMTEwLjgxIDEzLjYwTDExMy4xNSAxMy42MEwxMTYuODcgMjJMMTE0LjQwIDIyTDExMy43NCAyMC4zN0wxMTAuMTkgMjAuMzdMMTA5LjUzIDIyWk0xMTEuOTYgMTUuOTNMMTEwLjg4IDE4LjYxTDExMy4wNCAxOC42MUwxMTEuOTYgMTUuOTNaTTEyMi44MSAxNS40OEwxMjAuMjMgMTUuNDhMMTIwLjIzIDEzLjYwTDEyNy43NSAxMy42MEwxMjcuNzUgMTUuNDhMMTI1LjE5IDE1LjQ4TDEyNS4xOSAyMkwxMjIuODEgMjJMMTIyLjgxIDE1LjQ4Wk0xMzQuNTAgMjJMMTMyLjEzIDIyTDEzMi4xMyAxMy42MEwxMzQuNTAgMTMuNjBMMTM0LjUwIDE2Ljc2TDEzNy43NCAxNi43NkwxMzcuNzQgMTMuNjBMMTQwLjEyIDEzLjYwTDE0MC4xMiAyMkwxMzcuNzQgMjJMMTM3Ljc0IDE4LjcyTDEzNC41MCAxOC43MkwxMzQuNTAgMjJaIiBmaWxsPSIjRkZGRkZGIiB4PSI5MS45OSIvPjwvc3ZnPg==)](https://forthebadge.com)

</div>

- [⏯ Introdução](#-introdução)
- [📄 Arquivos](#-arquivos)
  - [*main.py*](#mainpy)
  - [src/](#src)
    - [*finite_elements.py*](#finite_elementspy)
    - [*matrixes.py*](#matrixespy)
    - [*integrals.py*](#integralspy)
    - [*preprocessing_data.py*](#preprocessing_datapy)
  - [*tests/*](#tests)
    - [*finite_e_tests.py*](#finite_e_testspy)
    - [*matrixes_tests.py*](#matrixes_testspy)
    - [*integrals_tests.py*](#integrals_testspy)
- [🚀 Execução](#-execução)
- [✨ Contribuidores](#-contribuidores)

## ⏯ Introdução

Este projeto se refere às tarefas da matéria de MAP3121 - Métodos Numéricos e Aplicações. Na primeira tarefa, foi proposta a realização de um projeto capaz de gerar as matrizes e resolver um sistema tridiagonal cíclico a partir da decomposição LU desse sistema. Na segunda tarefa, foi proposta a realização de um algoritmo que utiliza as formulas de Gauss para calcular integrais duplas. Para realizar a verificação do algoritmo, foram feitos diversos testes propostos. Já na terceira, foi proposta a utilização do método dos elementos finitos para calcular a variação de temperatura em um chip.

## 📄 Arquivos

Para facilitar a organização do código, e modularizá-lo melhor para a realização do próximo exercício, os arquivos foram dividos em pastas e com uma *main.py* que permite observar os resultados dos testes realizados.
```

├── .gitignore
├── src/
    ├── finite_elements.py
    ├── integrals.py
    ├── matrixes.py
    ├── preprocessing_data.py
├── tests/
    ├── finite_e_tests.py
    ├── integrals_tests.py
    ├── matrixes_tests.py
├── README.md
├── dados.txt
└── main.py
```

### *main.py* 
Código principal do projeto. Ao rodar ele, você pode escolher entre três modos:

<ol>
<li> Matrizes: Realiza os testes implementados para as matrizes, que incluem a resolução de um sistema tridiagonal cíclico e uma verificação do tempo do algoritmo
<li> Integrais: Imprime a resolução dos 4 exemplos requisitados pelo exercício programa
<li> Integrais: Imprime as resoluções dos exercícios propostos pelo exercício programa 3, contendo os gráficos e erros para as equações com ou sem forçantes de calor, e também abrange as que possuem variação de material
</ol>

### src/
Agrupa as funções utilizadas nos três exercícios programas. 

#### *finite_elements.py*
Possui as funções utilizadas para realizar o cálculo do método dos elementos finitos.
#### *matrixes.py*
Possui as funções utilizadas para calcular os vetores, decomposições e o sistema das matrizes tridiagonais.
#### *integrals.py*
Contém a função da formula de Gauss, responsável por resolver integrais duplas por meio da somatória entre intervalos ajustados.
#### *preprocessing_data.py*
Faz o processamento dos dados.txt que contem os pesos utilizados na formula de Gauss, transformando o txt em 3 dataframes diferentes

### *tests/* 
Agrupa os testes utilizados para verificar os algoritmos.

#### *finite_e_tests.py*
Realiza os testes, plotando os gráficos para as equações apresentadas e também para as forçantes de calor. ALém disso, calcula o erro entre as curvas teóricas e calculadas.

#### *matrixes_tests.py*
Realiza os testes gerando uma matrix tridiagonal cíclica e resolvendo seu sistema. Também checa o tempo de funcionamento do algoritmo.

#### *integrals_tests.py*
Realiza os testes para verificar o algoritmo de cálculo de integrais duplas. Verifica o volume de um cubo a partir de uma aresta, volume de um tetraedro a partir de seus vértices, volume de uma superfície descrita por uma função exponencial e o volume da calota e do sólido de revolução descritos no Exemplo 4.

## 🚀 Execução

Basta executar o arquivo *main.py* por meio da linha de comando abaixo:
```[python3]
python main.py
```

## ✨ Contribuidores
Um agradecimento aos contribuidores do projeto:
<table>
<tr>
<td align="center"><a href="https://github.com/mariarezende07"><img src="https://avatars.githubusercontent.com/u/54939351?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Maria Fernanda Rezende</b></sub></a><br /><a href="#" title="Code">💻</a> <a href="#" title="Documentation">📖</a></td>

<td align="center"><a href="https://github.com/MathTakaki"><img src="https://avatars.githubusercontent.com/u/89594894?v=4" width="100px;" alt=""/><br /><sub><b>Matheus Takaki</b></sub></a><br /><a href="#" title="Code">💻</a> <a href="#" title="Documentation">📖</a></td>
</tr>
</table>