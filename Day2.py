f = open("Day2_Data.txt")


data = [line.split("x") for line in f.read().split("\n")]

area = 0
print(data[1])
for j in data:
    i = [int(el) for el in j]
    #p = [i[1]*i[2]*2, i[1]*i[3]*2, i[2]*i[3]*2]    
    #p = sum(p) + min(p)

    #area += p

print(area)    
