#to check if a number is a perfect number , the sum of divisors of a number is equal to the number itself
num = int(input("Enter a number: "))
divisors = []

for i in range(1,num):
    if num % i == 0:
        divisors.append(i)

if sum(divisors) == num:
    print("Its a Perfect Number!!!")
else:
    print("Its not a Perfect Number!!!!")