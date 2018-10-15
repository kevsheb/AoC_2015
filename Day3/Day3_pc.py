f = list(open('Day3_Data.txt','r').read())

currpos = [0,0]
listpos = [currpos]
movepos = {'>':[1,0], '^':[0,1], '<':[-1,0], 'v':[0,-1]}

for ii in f:
    nextpos = [a+b for a,b in zip(currpos,movepos[ii])]
    listpos += [nextpos]
    currpos = nextpos

print(len(set([tuple(x) for x in listpos])))
