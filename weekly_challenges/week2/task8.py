#grades
mark = int(input("Enter your mark ( out of 100 ) : "))

if mark < 25 :
    print("Grade : F")
elif 25 <= mark < 45:
    print("Grade : E")
elif 45 <= mark < 50:
    print("Grade : D")
elif 50 <= mark < 60:
    print("Grade : C")
elif 60 <= mark < 80:
    print("Grade : B")
elif 80 <= mark < 100:
    print("Grade : A")
else:
    print("Entered mark is outside of range!!!")
