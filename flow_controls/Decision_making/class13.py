#calculate electricity bill
#first 100 units is free
#101 - 200 5rs per unit
#above 200 10rs per unit

# consumption = int(input("Enter the amount of units used:"))
# amount = 0
#
# if consumption <= 100:
#     amount = 0
# elif(consumption >101) & (consumption <= 200):
#     temp = consumption % 100
#     amount = amount + (temp * 5)
# elif consumption > 200:
#     temp = consumption % 200
#     amount = amount + (99 * 5)
#     amount = amount + (temp * 10)
# print("price is :",amount)

consumption = int(input("Enter the amount of units used:"))

if consumption <= 100:
    amount = 0
elif(consumption >101) & (consumption <= 200):
    amount = (consumption-100) * 5
else:
    amount = (consumption-200) * 10 +500
print("price is :",amount)