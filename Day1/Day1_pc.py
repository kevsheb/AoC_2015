# Day 1
f = list(open('Day1_Data.txt','r').read())

# Floor landing
floor = f.count('(')-f.count(')')
print('Floor landing = %s' %floor)

# Basement landing
ud     = {'(':1,')':-1}
lcount = 0
for base,ll in enumerate(f):
    if lcount > -1:
        lcount += ud[ll]
    else:
        break
    
print('Basement landing = %s' %base)
