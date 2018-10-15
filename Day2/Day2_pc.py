import pandas as pd

f = pd.read_csv('Day2_Data.txt',delimiter='x',header=None)
f[10] = 2*f[0]*f[1]
f[12] = 2*f[1]*f[2]
f[20] = 2*f[0]*f[2]
f[99] = f[[10,12,20]].min(axis=1)/2
f[[10,12,20,99]].sum().sum()
