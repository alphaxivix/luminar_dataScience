#sum of all even numbers from lower limit to upper

lower = int(input("Enter the lower limit:"))
upper = int(input("Enter the upper limit:"))
sum_o = 0
sum_e = 0
for i in range(lower,upper+1):
    if i%2 == 0:
        sum_e += i
    else:
        sum_o += i

print("sum of even numbers:",sum_e)
print("sum of odd numbers:",sum_o)