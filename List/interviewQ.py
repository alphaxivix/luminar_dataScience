#Q. we need to find the relation between two list and implement the logic
    # lst = [12,8,3,10,7,15,5]
    # lst1 = [48,52,57,50,53,45,55]

    # here we need to find the relation between the two lists
    # the sum of the first list is used to print the difference of each elements

lst = [12,8,3,10,7,15,5]
sum = sum(lst)
lst1 = [sum - i for i in lst]
print(lst1)