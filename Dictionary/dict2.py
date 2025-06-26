dict = {'id' : 101, 'name' : 'Abel', 'Age' : 20}
print(dict)

#a dictionary supports heterogeneous data

dict['id'] = 102
print(dict)

dict['Gender'] = "Male"
print(dict)

dict['Age'] = 28
print(dict)

dict['age'] = 28
print(dict)

for i in dict:
    print(i,dict[i],",")