f = open("Day2_Data.txt")

data = [line.split("x") for line in f.read().split("\n")]

area = 0
length = 0

for j in data:
    i = [int(el) for el in j] 
    p = [i[0]*i[1]*2, i[0]*i[2]*2, i[1]*i[2]*2]    
    p = sum(p) + min(p)/2
    area += p

    i.sort()
    length += 2*(i[0] + i[1]) + i[0]*i[1]*i[2]
    
    
print(area)   
print(length)

 
