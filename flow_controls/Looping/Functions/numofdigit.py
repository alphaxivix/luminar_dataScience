def length(n):
    digits = 0

    while n != 0:
        digits += 1
        n = n // 10
    return digits

num = int(input("Enter a number:"))
print("Length of the number is : ",length(num))



