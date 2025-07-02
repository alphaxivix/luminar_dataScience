# rating above 4
# before 2000 , name , year , duration
# each year release movie count
# release year above 2005 and rating above 4 , year , rating
# A letter movies collect
from calendar import month

f = open("C:/Users/alpha/Downloads/movies_cleaned_pandas.csv","r")

# for i in f :
#     data = i.rstrip("\n").split(',')
#     if data[3] > '4':
#         print(data[1],data[3])

# for i in f:
#     data = i.rstrip('\n').split(',')
#     if data[2] < "2000" and data[3] > '4':
#         print(data[1:4])

# mov_count = {}
# for i in f:
#     data = i.rstrip('\n').split(',')
#     year = data[2]
#     if year not in mov_count:
#         mov_count[year] = 1
#     else :
#         mov_count[year] += 1
# for i in mov_count:
#     print(i,":",mov_count[i])

# for i in f :
#     data = i.rstrip('\n').split(',')
#     year = data[2]
#     rating = data[]
#     if year > '2005' and rating >

mov_count = {}
for i in f:
    data = i.rstrip('\n').split(',')
    Alpha = data[1][1]
    if Alpha in 'aA':
        mov_count[year] = 1
    else :
        mov_count[year] += 1