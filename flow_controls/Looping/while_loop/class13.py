#lower to upper range
#read lower limit upper limit , display even numbers upto upper limit

lower = int(input("Enter the lower limit:"))
upper = int(input("Enter the upper limit:"))

while lower <= upper:
    if(lower %5 == 0):
        print(lower)
    lower += 1