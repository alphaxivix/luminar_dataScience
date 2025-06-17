x = 10      #Global Variable

def myfun():
    x = 5   #Local variable
    print("value of x inside function =",x)

print("Value of x outside function = ",x)
myfun()