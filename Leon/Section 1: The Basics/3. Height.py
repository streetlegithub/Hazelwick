# get name and height
name = input("What is your name? ")
height = int(input("Enter your height in cm: "))
# constant for cm to inch calculation
CM_TO_INCH = 2.54
# get total in inches
inches = float(height/CM_TO_INCH)
# print useful information
print(f"Hi {name.title()}!")
print(f"Your height is {height/100} m.")
print(f"That is {inches:.2f} inches.")
print(f"Taller than 180 cm: {height > 180}")
# extension
print(f"That is {int(inches//12)} feet {float(inches % 12):.1f} inches")
