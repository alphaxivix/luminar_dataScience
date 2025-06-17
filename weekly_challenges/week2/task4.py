#wage calculator , age between 18 and 30 for male 700 and female 750 , and age between 30 and 40 , for male 800 and female 850 per day....
# we have to calculate the total wages for prompted number of days
age = int(input("Enter your age :"))
days = int(input("Enter the number of days :"))
gender = input("Enter your gender ('M' for Male and 'F' for Female)  :")
if 18 <= age < 30:
    if gender == 'M' or gender == 'm':
        total_wage = days * 700
        print("Total wage :", total_wage)
    elif gender == 'F' or gender == 'f':
        total_wage = days * 750
        print("Total wage : ", total_wage)
elif 30 <= age < 40:
    if gender == 'M' or gender == 'm':
        total_wage = days * 800
        print("Total wage :", total_wage)
    elif gender == 'F' or gender == 'f':
        total_wage = days * 850
        print("Total wage : ", total_wage)
