# set current year as a constant
YEAR = 2026
# get name and d.o.b values from user
name = input("Enter your name: ")
born = int(input("Enter the year you were born: "))
# print final output using values
print(f"Hello {name}, you will be {YEAR-born} this year.")
