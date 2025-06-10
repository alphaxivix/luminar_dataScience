# Logical Operators are used to perform logical operations on two numbers/values
# some logical operators are :
#     i. AND ( symbol - & ) //does logical AND operations on two values
#     ii. OR ( symbol - | ) //does logical OR operations on two values
#     iii. XOR ( symbol - ^ ) //does logical XOR operations on two values

# i. AND &
#
# Truth Table for AND Operation
# I/P                  O/P
# 0       0            0
# 0       1            0
# 1       0            0
# 1       1            1

num1 = 2    #0010
num2 = 4    #0100
print(num1&num2) #output : 0 binary value obtained after AND operation : 0000

num3 = 1    #0001
num4 = 1    #0001
print(num3&num4)    #output : 1     binary value obtained after AND operation : 0001