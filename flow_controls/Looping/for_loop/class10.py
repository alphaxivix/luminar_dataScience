#even numbers from lower to upper
lower = int(input("Enter the lower limit :"))
upper = int(input("Enter the upper limit :"))

for i in range(lower,upper+1):
    if i % 2 == 0:
        print(i)

