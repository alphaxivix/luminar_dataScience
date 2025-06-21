#count the digits in a number

num = int(input("Enter a number: "))
temp,count = num,0
while num > 0:
    digits = num % 10
    count += 1
    num //= 10

print(f"Number of digits in this number is : {count}")