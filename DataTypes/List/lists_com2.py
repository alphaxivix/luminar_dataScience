#print the squares of even numbers in a list using comprehension

numbers = [1,2,3,4,5,6]

res = [i * i for i in numbers if i % 2 == 0]
print(res)
print(sum([i * i for i in numbers if i % 2 == 0]))