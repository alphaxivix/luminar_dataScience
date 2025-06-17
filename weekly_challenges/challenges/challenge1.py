count = 0
while True:
    name = input("Enter the name of the person you want to invite:")
    print("You have invited ",name)
    count += 1
    inv = input("Do you want to invite someone else??\n Enter Y (yes) or N (no) :")
    if inv == 'Y' or inv == 'y':
        continue
    else :
        break
print("People count: ",count)
