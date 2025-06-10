#calculate age
# read from console --> current_year, current_month, current_date, birth_year, birth_month, birth_date
# find the age of that person based on year, month, and date

cur_yr = int(input("enter current year:"))
cur_mnth = int(input("enter current month:"))
cur_date = int(input("enter current date:"))
b_yr = int(input("enter your birth year:"))
b_mnth = int(input("enter your birth month:"))
b_date = int(input("enter your birth date:"))

age = cur_yr - b_yr

if cur_mnth == b_mnth:
    if cur_date < b_date:
        age -= 1
elif cur_mnth < b_mnth :
    age -= 1

print("Your age is :",age,"years......")
