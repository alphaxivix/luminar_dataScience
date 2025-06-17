#print total until sum gets to 50
total = 0
while total <= 50:
    num = int(input("Enter a number: "))
    total += num
    print("\t\tTotal is : ",total)
print("Total values exceeded limit (50)")