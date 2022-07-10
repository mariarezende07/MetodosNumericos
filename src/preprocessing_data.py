import pandas as pd
import numpy as np

# Lê os dados txt, considerando tabs e espaços como separadores, e define as colunas
data = pd.read_csv('dados.txt', sep='\s+', names=["x_j","w_j"])
# As colunas que contém as strings 'n=6', 'n=8' e 'n=10' fazem pares com dados NaN. 
# Para facilitar a limpeza, vamos excluir todos os dados não válidos
data = data.dropna()
# Também excluimos os dados que tem apenas os nomes das colunas duplicados
data = data.drop(data[data.values == ["x_j"]].index).reset_index(drop=True)
# Convertemos as strings para doubles longos com dupla precisão
data = data.astype(np.longdouble)
# Para facilitar o manuseio, vamos gerar os dados simétricos e agrupá-los com os outros pontos
simetric_data = data.copy()
simetric_data["x_j"] = simetric_data['x_j'].apply(lambda x: x*-1)

data = pd.concat([data,simetric_data]).sort_index()

# Separamos, por posição, os dados de n=6, n=8 e n=10
n2 = data.loc[0].reset_index(drop=True).sort_values(by=['x_j'])
n6 = data.loc[1:3].reset_index(drop=True).sort_values(by=['x_j'])
n8 = data.loc[4:7].reset_index(drop=True).sort_values(by=['x_j'])
n10 = data.loc[8:12].reset_index(drop=True).sort_values(by=['x_j'])

print(f"n2= {n2}\nn6 ={n6} \nn8 = {n8} \nn10 = {n10}")