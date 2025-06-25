#Finding elements in a list using comparison operator

lst = [1,4,3,2,5,6,77,64,98]
num = int(input("Enter a value: "))
flag = False

for i in lst:
    if i == num:
        flag = True
if flag:
    print("Element found!")
else:
    print("Element not found!!")