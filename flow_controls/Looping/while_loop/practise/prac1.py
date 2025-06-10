#check if a number is a palindrome
num = int(input("Enter a number:"))
rev,temp = 0,num
while num != 0:
    digit = num % 10
    rev = (rev*10) + digit
    num //= 10

if temp == rev :
    print("The number is a palindrome!!")
else:
    print("Not a palindrome!!")