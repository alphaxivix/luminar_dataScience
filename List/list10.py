# lst = [i for i in range(1,101)]
# lst_even = [i for i in lst if i % 2 == 0]
# lst_odd = [i for i in lst if i % 2 == 1]

lst = []
lst_even = []
lst_odd = []

for i in range(1,101):
    lst.append(i)
    if i % 2 == 0:
        lst_even.append(i)
    elif i % 2 != 0:
        lst_odd.append(i)

print("The list:",lst)
print("The odd numbers:", lst_odd)
print("The even numbers:", lst_even)

print("Sum of the list:",sum(lst))
print("Sum of the odd numbers:",sum(lst_odd))
print("Sum of the even numbers:",sum(lst_even))

# for i in range(1,1000):
#     if i < 0:
#         print("fh")
# print(i)
#=================NOTE : after a loop is iterated upto the range the value of the counter will be equal to the condition max val