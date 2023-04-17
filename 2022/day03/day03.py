import string
with open ('input.txt') as f:
    lines = f.readlines()

# Exercise 1
print("Exercise 1:")

'''
convert string to list
divide list in 2 even parts
compare if item in first_half (fh) is also in second_half (sh)
create dictionary of items and weights
track total_priority (tp)
'''

#print(lines[0])
# convert string to list
#items = list(lines[0])
#print(items[:-1])

tp=0
#create dictionary of items and weights
lower_weights = dict()
for index, letter in enumerate(string.ascii_lowercase):
    lower_weights[letter] = index + 1

upper_weights = dict()
for index, letter in enumerate(string.ascii_uppercase):
    upper_weights[letter] = index + 27

# divide list in 2 even parts
for i in range(len(lines)):
    items = list(lines[i])
#    count = len(items[:-1])//2
#    print("the count is: " +str(count))
    fh = set(items[0:len(items)//2])
    sh = set(items[len(items)//2:-1])
    print(fh)
    print(sh)
#compare if item in first_half (fh) is also in second_half (sh)
    for j in fh:
        if j in sh:
            print("the letter " + j + " is in both lists")
            if j in lower_weights:
                print(lower_weights[j])
                tp += (lower_weights[j])
            if j in upper_weights:
                print(upper_weights[j])
                tp += (upper_weights[j])

print(tp)


# Exercise 2
print("Exercise 2:")

'''
reset tp
divide input into groups of 3
compare if item in first_group (fg) is also in second_group (sg) and is also in third group (tg)
get total priority (tp)
'''

tp = 0

# divide list in groups of 3
for i in range(len(lines)):
    while lines:
        group = lines[0:3]
        lines.pop(2)
        lines.pop(1) 
        lines.pop(0)
    #    print(group)
        fg = group[0]
        sg = group[1]
        tg = group[2]
        print(fg)
        print(sg)
        print(tg)

        #compare if item in first_group (fg) is also in second_group (sg) and is also in third group (tg)
        done = []
        for j in fg:
            if j in sg:
                if j in tg:
                    if j not in done:
                        print(tp)
                        print("the letter " + j + " is in all 3 lists")
                        if j in lower_weights:
                        #print(lower_weights[j])
                            tp += (lower_weights[j])
                        if j in upper_weights:
                        #print(upper_weights[j])
                            tp += (upper_weights[j])
                        done.append(j)

print(tp)
