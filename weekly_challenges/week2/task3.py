#to find the greatest number among three numbers
num1 = int(input("Enter first number:"))
num2 = int(input("Enter Second number:"))
num3 = int(input("Enter three number:"))

if num1 > num2 and num1 > num3 :
    print(num1, 'is the greatest number')
elif num2 > num1 and num2 > num3 :
    print(num2 , 'is the greatest number')
else:
    print(num3 , 'is the greatest number')