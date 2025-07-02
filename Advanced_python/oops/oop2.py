

class Person:
    def setvalues(self, fname,lname,age,phno):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.phone = phno

    def printvalues(self):
        print(self.fname,self.lname,self.phone,self.age)

person1 = Person()
person1.setvalues('Abel','cp',20,9947858883)
person1.printvalues()


person2 = Person()
person2.setvalues('Albin','Davis',21,4348344)
person2.printvalues()


person1.setvalues('Alpha','xivix',23,345245)
person1.printvalues()
