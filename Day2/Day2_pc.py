# Day 2
import pandas as pd
f = pd.read_csv('Day2_Data.txt',delimiter='x',
                header=None,names=['l','w','h'])

# Wrap area
f['lw'] = 2*f['l']*f['w']
f['wh'] = 2*f['w']*f['h']
f['hl'] = 2*f['h']*f['l']
f['a']  = f[['lw','wh','hl']].min(axis=1)/2
wrap    = int(f[['l','w','h','a']].sum().sum())
print('Wrap area = %s' %wrap)

# Ribbon length
f['d'] = 2*(f[['l','w','h']].sum(axis=1)-f[['l','w','h']].max(axis=1))
f['lwh']  = f['l']*f['w']*f['h']
ribbon    = int(f[['d','lwh']].sum().sum())
print('Ribbon length = %s' %ribbon)
