#to display the first recursive character in the given string

pattern = "ABCDBCDAFSDFJ"
dict = {}
for i in pattern:
    if i not in dict:
        dict[i] = 1
    else:
        print(f"{i} is the first recursive character!!")
        break