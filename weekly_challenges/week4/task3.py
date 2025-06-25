count = 4
for i in range(0,7):
    if i < 4:
        for _ in range(i,4):
            print("*", end=" ")
    elif i >= 4:
        for _ in range(4,i+2):
            print("*",end=" ")
    print()