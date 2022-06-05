<h1 align="center">
    🔢 Exercício programa de Métodos Numéricos
</h1>

<div style="text-align:center">

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)

</div>

- [⏯ Introdução](#-introdução)
- [📄 Arquivos](#-arquivos)
  - [*main.py*](#mainpy)
  - [src/](#src)
    - [*matrixes.py*](#matrixespy)
    - [*integrals.py*](#integralspy)
    - [*preprocessing_data.py*](#preprocessing_datapy)
  - [*tests/*](#tests)
    - [*matrixes_tests.py*](#matrixes_testspy)
    - [*integrals_tests.py*](#integrals_testspy)
- [🚀 Execução](#-execução)
- [✨ Contribuidores](#-contribuidores)

## ⏯ Introdução

Este projeto se refere às tarefas 01 e 02 da matéria de MAP3121 - Métodos Numéricos e Aplicações. Na primeira tarefa, foi proposta a realização de um projeto capaz de gerar as matrizes e resolver um sistema tridiagonal cíclico a partir da decomposição LU desse sistema. Na segunda tarefa, foi proposta a realização de um algoritmo que utiliza as formulas de Gauss para calcular integrais duplas. Para realizar a verificação do algoritmo, foram feitos diversos testes propostos.

## 📄 Arquivos

Para facilitar a organização do código, e modularizá-lo melhor para a realização do próximo exercício, os arquivos foram dividos em pastas e com uma *main.py* que permite observar os resultados dos testes realizados.
```

├── .gitignore
├── src/
    ├── integrals.py
    ├── matrixes.py
    ├── preprocessing_data.py
├── tests/
    ├── integrals_tests.py
    ├── matrixes_tests.py
├── README.md
├── dados.txt
└── main.py
```

### *main.py* 
Código principal do projeto. Ao rodar ele, você pode escolher entre dois modos:

<ol>
<li> Matrizes: Realiza os testes implementados para as matrizes, que incluem a resolução de um sistema tridiagonal cíclico e uma verificação do tempo do algoritmo
<li> Integrais: Imprime a resolução dos 4 exemplos requisitados pelo exercício programa
</ol>

### src/
Agrupa as funções utilizadas nos dois exercícios programas. 

#### *matrixes.py*
Possui as funções utilizadas para calcular os vetores, decomposições e o sistema das matrizes tridiagonais.
#### *integrals.py*
Contém a função da formula de Gauss, responsável por resolver integrais duplas por meio da somatória entre intervalos ajustados.
#### *preprocessing_data.py*
Faz o processamento dos dados.txt que contem os pesos utilizados na formula de Gauss, transformando o txt em 3 dataframes diferentes

### *tests/* 
Agrupa os testes utilizados para verificar os algoritmos.

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