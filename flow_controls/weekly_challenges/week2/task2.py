#check if a year is a leap year or not
yr = int(input("Enter the year :"))

if yr % 4 == 0 and yr % 100 != 0:
    print("This is a leap year!!")
elif yr % 4 == 0 and yr % 100 == 0:
    if yr % 400 == 0:
        print("This is a leap year...")
else :
    print("This is not a leap year!!!")