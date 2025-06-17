#swapping without temporary variable
num1 = 50
num2 = 100
print("Before Swapping:")
print("Num1 =",num1)
print("Num2 =",num2)

num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

print("After swapping:")
print("Num1 =",num1)
print("Num2 =",num2)
