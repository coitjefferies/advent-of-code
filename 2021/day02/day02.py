with open ('input.txt') as f:
    lines = f.readlines()

# Exercise 1

x=0
y=0

for i in range(len(lines)):
    a=lines[i]
#    print(a)
    if a[0:2] == 'up':
        y -= int(a[3])
    if a[0:4] == 'down':
        y += int(a[5])
    if a[0:7] == 'forward':
        x += int(a[8])

print('x = ' + str(x))
print('y = ' + str(y))
print('total = ' + str(int(x) * int(y)))

# Exercise 2

x=0
aim=0
y=0

for i in range(len(lines)):
    a=lines[i]
#    print(a)
    if a[0:2] == 'up':
        aim -= int(a[3])
#        print(aim)
    if a[0:4] == 'down':
        aim += int(a[5])
#        print(aim)
    if a[0:7] == 'forward':
        x = x + int(a[8])
        y = y + (aim * int(a[8]))

print('x = ' + str(x))
print('aim = ' + str(aim))
print('y = ' + str(y))
print('total = ' + str(int(x) * int(y)))
