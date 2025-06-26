string = "cat rat dog rat dog cat lion lion cat cat dog dog jog jog fog fog"
word = string.split()
dict = {}

for i in word:
    if i not in dict:
        dict[i] = 1
    elif i in dict:
        dict[i] += 1

print(f"-------------The total number of word occurences------------ \n\n{dict}\n\n-------------------------------------------------------------")