#enter two numbers and operator sign and perform the operation

num1 = int(input("Enter first number     : "))
num2 = int(input("Enter second number    : "))
operator = input("Enter the operator     : ")

if operator == '+':
    print("The result is    : ",num1 + num2)
elif operator == '-':
    print("The result is    : ", num1 - num2)
elif operator == '*':
    print("The result is    : ", num1 * num2)
elif operator == '/':
    print("The result is    : ", num1 / num2)
elif operator == '%':
    print("The result is    : ", num1 % num2)
elif operator == '**':
    print("The result is    : ", num1 ** num2)
elif operator == '//':
    print("The result is    : ", num1 // num2)
else :
    print("Enter a valid operator!!!")


