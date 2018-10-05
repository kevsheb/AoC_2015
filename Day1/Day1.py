# Read in Data
f = open("Day1_Data.txt")

# Iterate over and count based on input
floor = 0
for j, i in enumerate(f.read()):
    if i == "(":
        floor += 1
    else:
        floor -= 1

    # Check to see if floor is -1
    if floor == -1:
        print(j + 1) 

# print(floor)


