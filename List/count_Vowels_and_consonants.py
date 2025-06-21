
string = "Luminar technolab"
count = 0
vowels = ['a','e','i','o','u']

for i in string:
    if i.lower() in vowels:
        count += 1

print(f"Total number of characters : {len(string)}")
print(f"Total number of Vowels : {count}")
print(f"Total number of consonants : {len(string)-count}") # consonants is the letters that are not vowels