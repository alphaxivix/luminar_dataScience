

f = open("C:/Users/alpha/Downloads/sample4.txt",'r')

# for i in f:
#     data = i.rstrip('\n').split(',')
#     age = data[3]
#     if age >= '24':
#         print(data)

# for i in f:
#     data = i.rstrip('\n').split(',')
#     age = data[3]
#     if age == '21':
#         print(data[1:5])

# for i in f:
#     data = i.rstrip('\n').split(',')
#     location = data[5]
#     if location == "Chennai":
#         print(data[1:4])

for i in f:
    data = i.rstrip('\n').split(',')
    location = data[5]
    if location == "Chennai":
        print(data[1:4])

for i in f:
    data = i.rstrip('\n').split(',')
    location,age = data[5], data[3]
    if location == "Chennai" and age > '23':
        print(data[1:5])