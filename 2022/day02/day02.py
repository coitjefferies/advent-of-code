with open ('input.txt') as f:
    lines = f.readlines()

# Exercise 1
print("Exercise 1:")

'''
if A = X, draw
if B = Y, draw
if C = Z, draw

X beats C
Y beats A
Z beats B

A beats Z
B beats X
C beats Y

X is worth 1pt
Y is worth 2pts
Z is worth 3pts

lose = 0pts
draw = 3pts
win = 6 pts
'''

#print(lines[0])

# to get my rounds choice
#print(lines[0][2])

# to get my opponents choice
#print(lines[0][0])

ts=0

for i in range(len(lines)):
    theirs=lines[i][0]
    mine=lines[i][2]

    if mine == "X":
        ts += 1
    elif mine == "Y":
        ts += 2
    elif mine == "Z":
        ts += 3

    if theirs == "A":
        if mine == "X":
            ts += 3
        if mine == "Y":
            ts += 6
        if mine == "Z":
            ts += 0


    if theirs == "B":
        if mine == "X":
            ts += 0
        if mine == "Y":
            ts += 3
        if mine == "Z":
            ts += 6


    if theirs == "C":
        if mine == "X":
            ts += 6
        if mine == "Y":
            ts += 0
        if mine == "Z":
            ts += 3

print(ts)
print("Exercise 2:")


ts=0

for i in range(len(lines)):
    theirs=lines[i][0]
    outcome=lines[i][2]

    if outcome == "X":
        if theirs == "A":
            mine = "C"
        elif theirs == "B":
            mine = "A"
        elif theirs == "C":
            mine = "B"
        ts += 0

    if outcome == "Y":
        if theirs == "A":
            mine = "A"
        elif theirs == "B":
            mine = "B"
        elif theirs == "C":
            mine = "C"
        ts += 3

    if outcome == "Z":
        if theirs == "A":
            mine = "B"
        elif theirs == "B":
            mine = "C"
        elif theirs == "C":
            mine = "A"
        ts += 6

    if mine == "A":
        ts += 1
    elif mine == "B":
        ts += 2
    elif mine == "C":
        ts += 3

print(ts)
