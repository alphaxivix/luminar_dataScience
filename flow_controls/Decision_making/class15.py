#find rhe second largest among 3 numbers using nested if.....statement

num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
num3 = int(input("Enter third number:"))

if (num1 > num2) & (num1 > num3):
    if num2 > num3:
        print(num2,"is the second largest")
    else:
        print(num3,"is the second largest")
elif (num2 > num1) & (num2 > num3):
    if num1 > num3:
        print(num1,"is the second largest")
    else:
        print(num3,"is the second largest")
else:
    if num1 > num2:
        print(num1,"is the second largest")
    else:
        print(num2,"is the second largest")
