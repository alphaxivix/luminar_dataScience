#password validation , should contain >= 8 characters and also must contain at least one digit

password = input("Enter your password:")
pass_len = len(password)
digit = [0,1,2,3,4,5,6,7,8,9]
if pass_len < 8 and all(c in digit for c in password) == False:
    print("This Password is not allowed [minimum 8 characters required and at least one digit is required!!]")
else:
    print("Password allowed")
