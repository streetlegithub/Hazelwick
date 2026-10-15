# ask for year
year = int(input("Enter a year: "))
# do various calculations to determine if leap year
if ((year % 4 == 0) and (year % 100 != 0)) or ((year % 4 == 0) and (year % 100 != 0) and (year % 400 == 0)):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")