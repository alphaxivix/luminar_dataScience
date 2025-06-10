lower = int(input("Enter the lower limit:"))
upper = int(input("Enter the upper limit:"))
sum = 0

while lower <= upper:
    if lower %2 == 0:
        sum += lower
    lower += 1

print("Sum of even numbers:",sum)