# get number and calculate variables
number = int(input("Enter a 3 digit number: "))
hundreds = number//100
tens = (number % 100)//10
units = (number % 100) % 10
sum = hundreds + tens + units
# print various facts
print(
    f"Hundreds: {hundreds}\nTens: {tens}\nUnits: {units}\nSum of digits: {sum}\nReversed: {str(number)[::-1]}\nEven number: {number % 2 == 0}")
