# set the vat rate as a constant
RATE = float(0.2)
# get the product information and calculate both subtotal and total
price = float(input("Enter the price of the item: £"))
quantity = int(input("Enter the quantity: "))
subtotal = price*quantity
vat = subtotal*RATE
print(
    f"Total before VAT: £{subtotal:.2f}\nVAT: £{vat:.2f}\nTotal including VAT: £{(subtotal+vat):.2f}")
