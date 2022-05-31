import numpy as np
import pandas as pd
from scipy.spatial import distance_matrix

df_1 = pd.read_excel(r'German Cities.xlsx')
df_2 = pd.read_excel(r'2392-cities problems.xlsx')
df_3 = pd.read_excel(r'a280.xlsx')

distance_matrix_1 = pd.DataFrame(distance_matrix(df_1.values, df_1.values), index=df_1.index, columns=df_1.index)
distance_matrix_2 = pd.DataFrame(distance_matrix(df_2.values, df_2.values), index=df_2.index, columns=df_2.index)
# distance_matrix_3 = pd.DataFrame(distance_matrix(df_3.values, df_3.values), index=df_3.index, columns=df_3.index)
# distance_matrix_3 = pd.DataFrame(distance_matrix(df_3.values, df_3.values), index=df_3.index, columns=df_3.index)

dm = pd.DataFrame(distance_matrix(df.values, df.values), index=df.index, columns=df.index)
dm = dm.to_numpy()
dm

fitness = 0
for i in range(dm.shape[0]):
    fitness += dm[i - 1][i]
print(fitness)



