# max age of all profession 
# location min age

f = open('C:/Users/alpha/Downloads/customer1.txt','r')
dic = {}
# for i in f:
#     data = i.rstrip("\n").split(',')
#     age = data[3]
#     prof = data[4]
#     if prof not in dic:
#         dic[prof] = age
#     else:
#         cur = dic[prof]
#         if age > cur:
#             dic[prof] = age
# for k,v in dic.items():
#     print(k,":",v)

for i in f:
    data = i.rstrip("\n").split(',')
    age = data[3]
    loc = data[-1]
    if loc not in dic:
        dic[loc] = age
    else:
        cur = dic[loc]
        if age < cur:
            dic[loc] = age
for k,v in dic.items():
    print(k,":",v)