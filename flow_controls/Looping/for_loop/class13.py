#Fibonacci series, 0 ,1 , 1(0 + 1),2,3,5,8,13,21 [ n + (n + 1) ]
num1 = 0
num2 = 1
limit = int(input("Enter the limit:"))
print(num1)
print(num2)
for i in range (3,limit+1):
    sum = num1 + num2
    num1 = num2
    num2 = sum
    print(sum)
