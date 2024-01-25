#variable declarations
commissionRatePurchase = 0.0
commissionRateSale = 0.0
sharesPurchase = 0.0
sharesSold = 0.0
sharePrice = 0.0

#inputs
a = float(input("Enter commission rate percentage (ex 0.03) on stock purchase: "))
b = float(input("Enter commission rate percentage (ex 0.03) on stock sale: "))
c = int(input("Enter number of shares purchase: "))
d = int(input("Enter number of shares sold: "))
e = float(input("Enter purchase price per share: "))
f = float(input("Enter sell price per share: "))

#calculations
stockPrice = c * e
commissionPurchase = stockPrice * a
stockSold = d * f
commissionSale = stockSold * b
profit = stockSold - stockPrice - commissionSale - commissionPurchase

#outputs
print('')
print(f'Amount paid for the stock: ${stockPrice:,.2f}')
print(f'Commission paid on the purchase: ${commissionPurchase:,.2f}')
print(f'Amount the stock sold for: ${stockSold:,.2f}')
print(f'Commission paid on the sale: ${commissionSale:,.2f}')
print(f'Profit (or loss if negative: ${profit:,.2f}')
