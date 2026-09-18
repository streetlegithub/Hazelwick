number = int(input("Enter a 3 digit number: "))
hundreds = number//100
tens = (number%100)//10
units = (number%100)%10
sum = hundreds + tens + units
print(f"Hundreds: {hundreds}")
print(f"Tens: {tens}")
print(f"Units: {units}")
print(f"Sum of digits: {sum}")
print(f"Reversed: {str(number)[::-1]}")
print(f"Even number: {number % 2 == 0}")