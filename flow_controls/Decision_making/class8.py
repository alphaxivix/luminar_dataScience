salary = int(input("Enter your salary:"))
yr_serv = int(input("Years of service in this company:"))

if(yr_serv >= 5):
    bonus = (salary * 5)/100
    new_salary = salary + bonus
    print("Bonus Applied:",new_salary)
else:
    print("Need more experience!!")