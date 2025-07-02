
f = open("C:/Users/alpha/Downloads/customer1.txt", 'r')
dict, dict_l = {}, {}
# for i in f:
#     data = i.rstrip('\n').split(',')
#     age, location = data[3], data[-1]
#     prof = data[-2]
#     if age > '50' :
#         print(data[1:5])

# for i in f:
#     data = i.rstrip('\n').split(',')
#     age, location = data[3], data[-1]
#     prof = data[-2]
#     if '25' < age < "40":
#         print(data[1:5])

#     if location == 'india':
#         print(f"Location India: \n {data[1:5]}")
#     if location == 'india' and age > '50':
#         print(f"Age = 50: \n {data[1:4]}")
#     if location == "uk":
#         print(f"Location UK: \n {data[1:5]}")

# for i in f:
#     data = i.rstrip('\n').split(',')
#     age, location = data[3], data[-1]
#     prof = data[-2]
#     if prof == "Doctor":
#         print(f"Profession Doctor: \n {data[1:4]}")


# for i in f:
#     data = i.rstrip('\n').split(',')
#     age, location = data[3], data[-1]
#     prof = data[-2]
#     if prof == "Doctor" and age < "40":
#         print(f"Doctor of age < 40 : \n {data[1:4]}")
#     if prof == "Pilot":
#         print(f"Profession Pilot: \n {data[1:4]}")

for i in f:
    data = i.rstrip('\n').split(',')
    age, location = data[3], data[-1]
    prof = data[-2]
    if prof not in dict:
        dict[prof] = 1
    elif prof in dict:
        dict[prof] += 1
    if location not in dict_l:
        dict_l[location] = 1
    if location in dict_l:
        dict_l[location] += 1
print(f"-------------------- Profession Count --------------- ")
for i in dict:
    print(i,":",dict[i])
print(f"-------------------- Location Count --------------- ")
for i in dict_l:
    print(i,":",dict_l[i])
#
