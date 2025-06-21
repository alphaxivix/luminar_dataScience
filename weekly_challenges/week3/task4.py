#armstrong number check

num = int(input("enter a number: "))
temp, sum = num,0
length = len(str(num))
while num > 0:
    digit = num % 10
    sum += digit ** length
    num //= 10
if sum == temp:
    print(f"The given number {temp} is an Armstrong number!")
else:
    print("The given number is not an Armstrong number!!")
