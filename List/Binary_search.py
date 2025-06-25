#the binary search algorithm implemented using both for and while loops 

lst = [1,2,4,6,11,12,10,23,43]
num = int(input("Enter a number: "))
lst.sort()
low, upper = 0 , len(lst)-1
flag = False

# mid = (low + upper) // 2
# if num > lst[mid]:
#     low = mid + 1
# elif num < lst[mid]:
#     upper = mid - 1
# elif num == lst[mid]:
#     print("Element Found")

# for i in range(low, upper):
#     if lst[i] == num :
#         flag = True

# if flag:
#     print("Element found")
# else:
#     print("Element not found")

while low<=upper:
    mid = (low+upper) // 2
    if num > lst[mid]:
        low = mid + 1
    elif num < lst[mid]:
        upper = mid - 1
    elif num == lst[mid]:
        flag = True
        break
if flag:
    print("Element found")
else:
    print("Element not found")
