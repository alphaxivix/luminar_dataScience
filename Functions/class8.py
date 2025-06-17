#Required parameters

def Addition(x, y):
    return x + y

def difference(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    return x / y
print("Enter two numbers:")
num1 = int(input("Enter number 1:"))
num2 = int(input("Enter number 2:"))
print("Enter your choice\n1.Addition\n2.Substraction\n3.multiplication\n4.Division")
choice = int(input("Your choice:"))

if choice == 1:
    print("Addition =",Addition(num1,num2))
elif choice == 2:
    print("Difference =",difference(num1,num2))
elif choice == 3:
    print("Multiplication = ",multiplication(num1,num2))
elif choice == 4:
    print("Division =",division(num1, num2))
else :
    print("Invalid choice!!")
