import pandas as pd
import numpy as np

data = pd.read_csv('dados.txt', sep='\s+', names=["x_j","w_j"])
data = data.dropna()
data = data.drop(data[data.values == ["x_j"]].index).reset_index(drop=True)

data = data.astype(np.longdouble)

simetric_data = data.copy()
simetric_data["x_j"] = simetric_data['x_j'].apply(lambda x: x*-1)

data = pd.concat([data,simetric_data]).sort_index()

n6 = data.loc[0:2].reset_index(drop=True).sort_values(by=['x_j'])
n8 = data.loc[3:6].reset_index(drop=True).sort_values(by=['x_j'])
n10 = data.loc[7:12].reset_index(drop=True).sort_values(by=['x_j'])



