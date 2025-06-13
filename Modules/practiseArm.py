#program to find armstrong numbers of range 100 to 1000

for i in range (100, 1000):
    sum_ = 0
    temp = i
    while i > 0 :
        digit = i % 10
        sum_ += digit ** 3
        i //= 10
    if temp == sum_ :
        print(temp)