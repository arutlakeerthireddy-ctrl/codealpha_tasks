prices={'AAPL':180,'TSLA':250,'GOOG':150,'MSFT':200}
total_investment=0
print("type 'done' to finish")
while True:
    stock=input("Enter stock name:").upper()
    if stock =='DONE':
        break
    if stock not in prices:
        print("stock not available")
        continue
    quantity=int(input("Enter quantity: "))
    total_investment+=quantity*prices[stock]
print('Total investment is :',total_investment)
with open('portfolio.txt','w') as f:
    f.write(f"Total investment is:{total_investment}")
print('data saved to portfolio.txt')
