#marksheet , grading based on average marks
print("Enter your marks (out of 100)")
sub_1 = float(input("Subject 1 :"))
sub_2 = float(input("Subject 2 :"))
sub_3 = float(input("Subject 3 :"))
sub_4 = float(input("Subject 4 :"))
sub_5 = float(input("Subject 5 :"))

avg_marks = (sub_1 + sub_2 + sub_3 + sub_4 + sub_5) / 5

print("Average mark :",avg_marks)

if 90 < avg_marks <= 100:
    print("A+")
elif 80 < avg_marks <= 89:
    print("A")
elif 70 < avg_marks <= 79:
    print("B")
elif 60 < avg_marks <= 69:
    print("C")
elif 50 < avg_marks <= 59:
    print("D")
else:
    print("F")