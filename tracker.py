stock_prices= {
    "AAPL":180,
    "TSLA":250,
    "GOOGL":140,
    "AMZN":170,
    "MSFT":420

}

total_investment=0
print("Stock Protofolio Tracker")
print("Available stocks:",",".join(stock_prices.keys()))

while True:
    stock=input("\n Enter stock name:").upper()

    if stock == "DONE":
        break

    if stock in stock_prices:
        quantity=int(input("Enter quantity:"))
        investment=stock_prices[stock]*quantity
        total_investment+=investment

        print("Investment for ",stock,":",investment)
    else:
        print(" stock not available.") 
print("\n Total Investment Value :",total_investment)           
