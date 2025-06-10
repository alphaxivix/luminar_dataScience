#sum of n numbers,

n = int(input("Enter the number:"))

i,sum = 1,0
while i <= n:
    sum = sum + i
    i += 1

print("the sum is", sum)