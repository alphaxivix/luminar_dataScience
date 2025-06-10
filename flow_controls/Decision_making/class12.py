#calculate road tax,
# read the price of a bike from console,
# if the price is above 1lak ==> tax 15% road tax of the price of bike
#if 50k - 100k tax ==> 10%
#if below 50k tax ==> 5%

price = int(input("enter the price of the bike:"))
if(price > 100000):
    tax_amnt = (price * 15)/100
elif(price >= 50000) & (price <= 100000):
    tax_amnt = (price * 10)/100
else:
    tax_amnt = (price * 5)/100

print("Road tax applicable :",tax_amnt)