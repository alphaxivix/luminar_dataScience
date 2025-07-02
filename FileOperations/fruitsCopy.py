fr = open('fruits','r')
fw = open('copyfr', 'w')

for i in fr:
    if 'apple' not in i.lower():
        fw.write(i)