with open ('input.txt') as f:
    lines = f.readlines()

# Exercise 1

calories=0
totalPerElf=[]

for i in range(len(lines)):
    if lines[i] == '\n':
        totalPerElf.append(calories)
        calories=0
    else:
        calories = calories + int(lines[i])

print(max(totalPerElf))

# Exercise 2

top3=[]

for i in range(3):
    most=[totalPerElf.pop(totalPerElf.index(max(totalPerElf)))]
    mostInt= int(most[0])
    top3.append(mostInt)

#top 3 are:
#print(top3)

#sum of top 3:
top3total=0
for i in range(len(top3)):
    top3total = top3total + int(top3[i])

print(top3total)

