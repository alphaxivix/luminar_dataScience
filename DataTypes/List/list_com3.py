#to print words that have more than 5 letters from a list

words = ["apple","banana","kiwi","strawberry","fig","grapes"]

res = [i.upper() for i in words if len(i) > 5]
print(res)
res.sort()
print(res)