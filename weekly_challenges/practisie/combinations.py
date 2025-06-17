#to characters combination

n = int(input("Enter the length of the combinations:"))
print("Enter",n,"characters:")
chars = []
for i in range(n):
    ch = input().strip()
    chars.append(ch)

print(chars)

r = n
num_combinations = n ** r
print(num_combinations)

for ch in chars:
    for c in chars:
        print(ch + c)

