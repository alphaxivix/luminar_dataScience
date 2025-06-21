# password validator that checks if the password given by the user has the following :
# * At least 1 lowercase letter, At least 1 uppercase letter, At least 1 digit,At least 1 special character ($#@ for example), Length at least 8 characters
def validator(ps):
    count_alp, count_digit, count_numeric, count_upper, count_lower = 0,0,0,0,0
    if len(ps) > 8 :
        for c in ps:
            if c.isalpha() :
                count_alp += 1
                if c.isupper():
                    count_upper += 1
                if c.islower():
                    count_lower += 1
            elif c.isdigit():
                count_digit += 1
                if c.isnumeric():
                    count_numeric += 1
        if count_alp > 0 and count_digit > 0 and count_numeric > 0 and count_upper > 0 and count_lower > 0:
            return True
        else :
            print("at least 1 alphabets (a-z)lowercase , 1 uppercase letter(A-Z), 1 digit(0-9), 1 special character (!@#$%^&*..) is required..............")
            return None
    else:
        print("at least 8 characters is required!!")
        return False

password = input("Enter New password: ")
if validator(password):
    print("PASSWORD VALIDATED SUCCESSFULLY")
else :
    print("Password Validation Failed!!")