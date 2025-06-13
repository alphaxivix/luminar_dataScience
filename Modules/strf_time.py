import datetime

x = datetime.datetime.now()

print(x.strftime("%a")) #here strftime() is used to get the string of the datetime values - a ==> abbri. day
print(x.strftime("%A"))
print(x.strftime("%b"))
print(x.strftime("%B"))
