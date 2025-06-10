# factorial of a number
n = int(input("Enter the number:"))

i, fact = 1, 1
while i <= n: fact = fact * i; i += 1;

print("the factorial is", fact)
