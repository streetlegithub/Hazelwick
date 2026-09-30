name = input("Name: ")
height = int(input("Height in cm: "))
CM_TO_INCH = 2.54
inches = float(height/CM_TO_INCH)
print(f"Hi {name.title()}!")
print(f"Your height is {height/100} m.")
print(f"That is {inches:.2f} inches.")
print(f"Taller than 180 cm: {height>180}")
# Extension
print(f"That is {int(inches//12)} feet {float(inches%12):.1f} inches")