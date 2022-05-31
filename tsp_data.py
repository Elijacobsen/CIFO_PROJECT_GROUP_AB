import pandas as pd
from scipy.spatial import distance_matrix

df_1 = pd.read_excel(r'berlin52.xlsx')
df_2 = pd.read_excel(r'pcb442.xlsx')
df_3 = pd.read_excel(r'xqf131.xlsx')

dm_1 = pd.DataFrame(distance_matrix(df_1.values, df_1.values), index=df_1.index, columns=df_1.index)
dm_1 = dm_1.to_numpy()

dm_2 = pd.DataFrame(distance_matrix(df_2.values, df_2.values), index=df_2.index, columns=df_2.index)
dm_2 = dm_2.to_numpy()

dm_3 = pd.DataFrame(distance_matrix(df_3.values, df_3.values), index=df_3.index, columns=df_3.index)
dm_3 = dm_3.to_numpy()
