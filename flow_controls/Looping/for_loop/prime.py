#to check whether a given number is prime or not

num = int(input("Enter a number:"))
flag = False

if num < 0:
    print("Enter a +ve number")
elif num == 0:
    print("You have entered zero")
elif num == 1:
    print("1 is a composite number")
else:
    for i in range(2,num):
        if num % i == 0:
            # print(num,"is not a prime number")
            flag = True
            break
    # else:
    #         #this else is nor paired with for-loop and not with if-statement
    #         print(num,"is prime")
if flag:
    print(num,"is not a prime number")
else:
    print(num,"is a prime number")