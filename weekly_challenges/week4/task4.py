n = 4
for i in range(1,5):
    c,k= 1,i
    for j in range(0,7):
        if j < n - i:
            print(" ",end="")
        if j == 3:
            print(i,end="")
        elif j >= n-i and j < 3:
            print(c,end="")
            c += 1
        elif j > 3:
            if k == 1:
                break
            k -= 1
            print(k,end="")
    print()