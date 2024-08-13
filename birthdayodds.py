import pandas as pd
import numpy as np
df = pd.read_csv("riffle_dist_table.csv")
df = df**2
average = 0
for i in range(52):
    sum = 0
    for j in range(52):
        sum+=df.iloc[i][j+1]
    average += sum/1000000000

print(average/52)
