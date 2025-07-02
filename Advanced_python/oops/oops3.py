
class Student:
    def setval(self, id, fname, lname, gender, course, colname):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.gender = gender
        self.course = course
        self.colname = colname

    def printval(self):
        print(self.id,self.fname,self.lname,self.gender,self.course,self.colname)

student1 = Student()
student1.setval(1,'Abel','CP','Male',"Bca","Ccsit")

student2 = Student()
student2.setval(2,'Albin','Davis','Male',"Mca","Ccsit")

student3 = Student()
student3.setval(3,'Baalan','KN','Male',"Bca","Kerala varma")

student4 = Student()
student4.setval(4,'Alpha','xivix','Male',"B.COM","Vidhya")

student5 = Student()
student5.setval(5,'Aryanandha','Biju','Female',"BSC","Sahradhaya")

student1.printval()
student2.printval()
student3.printval()
student4.printval()
student5.printval()