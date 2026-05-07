Cost_price=int(input("Enter the price : "))
Selling_price=int(input("Enter the price : ))
if Selling_price > Cost_price:
    profit = Selling_price - Cost_price
    profit_percentage = (profit/Cost_price)*100
    print("profit =" : profit)
    print("profit_percentage" : profit_percentage)
elif Selling_price < Cost_price:
    loss = Cost_price - Selling_price
    loss_percentage = (loss/Cost_price)*100
else:
    (NO profit and loss)