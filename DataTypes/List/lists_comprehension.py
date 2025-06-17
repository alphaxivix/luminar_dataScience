# list comprehension is used to simplify the lists operations, using a single line code
# syntax :
#         [expression for item in iterable if condition]

#this code creates a list that contains square of items 0 to 4

mlist = [x * x for x in range(5)]
print(mlist)