#marks of 4 subjects , total mark calculation , marks out of 50(per subject).
#if total >= 180 print A+, 160-179 A ,140-159 B+,120-139 B,100-119 C+,below 100 failed

sub1 = int(input("Enter mark of first subject:"))
sub2 = int(input("Enter mark of Second subject:"))
sub3 = int(input("Enter mark of Third subject:"))
sub4 = int(input("Enter mark of fourth subject:"))

total_marks = sub4+sub3+sub2+sub1
print("Total marks acquired:",total_marks)

if(total_marks >= 180):
    print("Grade: A+")
elif(total_marks >= 160) & (total_marks <=179):
    print("Grade:A")
elif(total_marks >= 140) & (total_marks <=159):
    print("Grade: B+")
elif(total_marks >= 120) & (total_marks <=139):
    print("Grade: B")
elif(total_marks >= 100) & (total_marks <=119):
    print("Grade: C+")
else:
    print("Failed!!")