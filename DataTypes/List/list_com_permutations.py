#to display permutations of x y and z , also a value n is read from the user , the combinations x + y + z == n is not allowed
#this program should use nested list comprehension

x = int(input("enter value for x : "))
y = int(input("enter value for y : "))
z = int(input("enter value for z : "))
n = int(input("enter value for n : "))

res = [[i,j,k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if x + y + z != n]

print(res)