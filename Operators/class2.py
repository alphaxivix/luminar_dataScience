#Logical operators
#some logical operators are : i.) AND &, ii.) OR | , iii.) XOR ^

# # AND operator ( & ) // produces a true output only if the both conditions are true
# 0       0       0
# 0       1       0
# 1       0       0
# 1       1       1
#
# # OR operator ( | pipe ) // produces a true output if any of the conditions is true also true if both conditions are true
# 0       0       0
# 0       1       1
# 1       0       1
# 1       1       1
#
# # XOR operator ( ^ cap ) // produces a true output only if the both conditions are different
# 0       0       0
# 0       1       1
# 1       0       1
# 1       1       0

# for eg

num1 = 7  # 0111
num2 = 6 # 0110
print(num1|num2) #O/P = 0111