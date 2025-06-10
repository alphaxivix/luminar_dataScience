#find the sum of digits until a single digit
# 9875 ==> 9+8+7+5 = 29 2+9 = 11 1+1 ==> 2
num = int(input("Enter a number:"))

while num >= 10:
    sum = 0
    t_num = num
    while t_num > 0:
        digit = t_num % 10
        sum += digit
        t_num //= 10
    num = sum

print(sum)