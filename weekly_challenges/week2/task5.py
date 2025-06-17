# calculate discount, if total purchase cost is > 1000 apply a 10 percentage discount

quantity = int(input("Quantity:"))
esti_cost = quantity * 100

if esti_cost > 1000 :
    disc_cost = 0.1 * esti_cost
    total_cost = esti_cost - disc_cost
    print("Estimated cost =",esti_cost)
    print("Discount applied (10%) =",disc_cost)
    print("Total Amount =",total_cost)
else:
    print("Total amount:",esti_cost)