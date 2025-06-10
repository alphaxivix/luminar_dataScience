total_class = int(input("Enter total number of class held:"))
attnded_class = int(input("How many classes have you attended??:"))

percen = (attnded_class/total_class)*100
print("percentage of attendance:",percen,'%')
if(percen > 75):
    print("eligible for exam!!")
else:
    print("not eligible!!")