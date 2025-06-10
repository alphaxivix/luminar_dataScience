num1 = int(input("Enter first number:"))
num2 = int(input("Enter Second number:"))

sum = lambda a,b : a + b
diff = lambda a,b : a - b
mul = lambda a,b : a * b
div = lambda a,b : a / b

print("Sum             :", sum(num1 , num2))
print("Difference      :", diff(num1 , num2))
print("Product         :", mul(num1 , num2))
print("Division        :", div(num1 , num2))
