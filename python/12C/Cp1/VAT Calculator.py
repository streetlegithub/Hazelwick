RATE = float(0.2)
price = float(input("Price: "))
quantity = int(input("Quantity: "))
subtotal = price*quantity
print(f"Total before VAT: £{subtotal}")
vat = subtotal/RATE
print(f"VAT: £{vat}")
print(f"Total including VAT: £{subtotal+vat}")