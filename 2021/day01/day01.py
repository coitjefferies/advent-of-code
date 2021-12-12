with open ('input.txt') as f:
    lines = f.readlines()

# Exercise 1

x=0
y=0
z=1

for i in range(len(lines)):
  if lines[i] > lines[i-1]:
    x += 1

print(x)

# Exercise 2

x=0
for i in range(len(lines) -2):
    prev_total=(int(lines[i]) + int(lines[i+1]) + int(lines[i+2]))
    total=(int(lines[i+1]) + int(lines[i+2]) + int(lines[i+3]))
    if total > prev_total:
        x += 1
    print(x)


# Not my best solution but I got the right number at the end...may come back to improve upon
