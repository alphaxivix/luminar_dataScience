#read 3 numbers and print the second-largest number
num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
num3 = int(input("Enter the third number:"))

if ((num1 > num3) & (num1 < num2)) | ((num1 < num3) & (num1 > num2)):
    print("The second largest number is:",num1)
elif ((num2 < num1) & (num2 > num3)) | ((num2 > num1) & (num2 < num3)):
    print("The second largest number is:",num2)
else:
    print("The second largest number is:",num3)