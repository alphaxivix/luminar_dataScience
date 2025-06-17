#we can delete items form list using several methods like
        #1. using del keyword
        #2. using remove()
        #3. using clear()

from DataTypes.List.lists_insertion import mylist

del mylist[0]
print(mylist)
mylist.remove("Alpha")
print(mylist)
mylist.clear()
print(mylist)
del mylist
print(mylist)