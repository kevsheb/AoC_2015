# Import Data
f = open("Day3_Data.txt")

x = 0
y = 0

houses = {0:{0:1}}

new_move = {'>':[1, 0],
            '<':[-1, 0],
            '^':[0, 1],
            'v':[0, -1]}

for i in f.read():
    direction = new_move[i]
    x += direction[0]
    y += direction[1]

    print(x, y)

    try:
        houses[x]

        try:
            houses[x][y] += 1
        except KeyError:
            houses[x][y] = 1

    except KeyError:
        houses[x] = {y:1}

sum = 0
for i in houses.keys():
    sum += len(houses[i].keys())


# Import Data and do robo santa
f = open("Day3_Data.txt")

x = 0
y = 0
rx = 0
ry = 0

houses = {0:{0:1}}
robo_houses = {0:{0:1}}

new_move = {'>':[1, 0],
            '<':[-1, 0],
            '^':[0, 1],
            'v':[0, -1]}

which_santa = 1
for i in f.read():
    direction = new_move[i]


    print(x, y)
    if which_santa == 1:
        x += direction[0]
        y += direction[1]
        which_santa *= -1

        try:
            houses[x]

            try:
                houses[x][y] += 1
            except KeyError:
                houses[x][y] = 1

        except KeyError:
            houses[x] = {y:1}

    else:
        which_santa *= -1
        rx += direction[0]
        ry += direction[1]
        try:
            houses[rx]

            try:
                houses[rx][ry] += 1
            except KeyError:
                houses[rx][ry] = 1

        except KeyError:
            houses[rx] = {ry: 1}

sum = 0
for i in houses.keys():
    sum += len(houses[i].keys())

print(sum)







