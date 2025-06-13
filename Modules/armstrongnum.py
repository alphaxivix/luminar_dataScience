num = int(input("Enter a number:"))

sum,temp = 0, num
while num > 0:
    digit = num % 10
    sum += digit ** 3
    num //= 10
if sum == temp:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number!!")