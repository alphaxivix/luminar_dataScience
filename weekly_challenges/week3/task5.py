#to print the numbers within a range except prime numbers
from math import sqrt
lower = int(input("enter the lower limit: "))
upper = int(input("enter the upper limit: "))
res = []
for i in range(lower,upper+1):
    if i<= 1:
        res.append(i)
    flag = False
    if i > 0:
        for j in range(2, int( sqrt(i) ) ):
            if i % j == 0:
                flag = True
                break
    if flag:
        res.append(i)
print(res)