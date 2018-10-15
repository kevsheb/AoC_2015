f = open('Day1_Data.txt','r')
f = list(f.read())
print(f.count('(')-f.count(')'))
