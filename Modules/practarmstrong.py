def length(i):
    count = 0
    while i != 0:
        count += 1
        i //= 10
    return  count

low = int(input("Enter lower limit:"))
upp = int(input("Enter upper limit:"))

for i in range(low, upp + 1):
    sum = 0
    temp = i
    leng = length(temp)
    while temp != 0 :
        # print("Temp =", temp)
        digits = temp % 10
        # print("Digit =",digits,"**",leng)
        sum += digits ** leng
        # print("sum =",sum)
        temp //= 10
    if i == sum:
        print(i)