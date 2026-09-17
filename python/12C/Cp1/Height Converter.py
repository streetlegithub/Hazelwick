name = input("Name: ")
height = int(input("Height in cm: "))
cmtoinch = 2.54
print(f"Hi {name.title()}!")
print(f"Your height is {height/100} m.")
print(f"That is {float(height/cmtoinch):.2f} inches.")
print(f"Taller than 180 cm: {height>180}")