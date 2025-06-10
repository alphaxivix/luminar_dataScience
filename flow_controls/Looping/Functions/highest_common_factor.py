def h_cf(x,y):
    if x < y :
        least = x
    else :
        least = y

    for i in range(1,least+1):
        if x % i == 0 and y % i == 0:
            hcf = i
    return hcf


num1 = int(input("Enter num1 : "))
num2 = int(input("Enter num2 :"))
high = h_cf(num1,num2)
print(high)