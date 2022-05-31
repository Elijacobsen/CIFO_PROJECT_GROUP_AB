import pandas as pd
import numpy as np

df = pd.read_csv(r'Performance_File.csv')
df.sort_values(by=['Avg_Fitness'], inplace=True)
df
