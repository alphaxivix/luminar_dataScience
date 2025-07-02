
f = open('numbers', 'r')
lst = []

#for i in f:
#     lst.append(int(i))

for i in f:
    lst.append(int(i.rstrip('\n')))

print(lst)
print(sum(lst))
