f =open('sample3' , 'r')
dict = {}

for i in f:
    data = i.rstrip('\n').split()
    for j in data:
        if j not in dict:
            dict[j] = 1
        else:
            dict[j] += 1
print(dict)
for i in dict:
    print(i," = ",dict[i])