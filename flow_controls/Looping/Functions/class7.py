#variable length arguments

def employee(name, *skills):
    print("Name   : ", name)
    print("Skills : ", skills)

employee("Abel", "python","C++","HTML","CSS")