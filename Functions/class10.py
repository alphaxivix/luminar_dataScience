# check if which num is greater , then greater%x & greater%y == 0 true ,find LCM

def gtr_num(x,y):
    if x > y:
        return x
    else:
        return y
def flcm(x , y):
    greater_num = gtr_num(x,y)
    while True :
        if greater_num % x == 0 and greater_num % y == 0:
            lcm = greater_num
            break
        greater_num += 1

    return lcm

num1 = int(input("Enter 1st number:"))
num2 = int(input("Enter 2nd number:"))

print(flcm(num1,num2))

