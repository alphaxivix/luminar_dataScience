lst = [1,3,6,5,4,3,4,6,8,9,10,11,9,7,6,5,6,8,9,15,14,12,11]

lst1 = [lst[i] for i in range(0,len(lst)-1) if lst[i] > lst[i+1] ]





print(lst1)