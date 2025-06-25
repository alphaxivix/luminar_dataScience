#create a new list that contains prime numbers of a given lists

lst = [2,34,54,3,4,5,6,353,34,22,44,33,7,1,0,153,231]

lst1 = [i for i in lst if i > 1 and all(i % n != 0 for n in range(2,i))]

print(f"The original List : {lst}")
print(f"The list of all prime numbers : {lst1}")