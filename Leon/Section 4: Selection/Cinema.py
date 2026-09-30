age = int(input("Enter your age: "))

if age <= 12:
    print("Ticket price: £5.00")
elif age < 17 and age > 12:
    print("Ticket price: £7.00")
elif age > 18 and age < 64:
    card = input("Student Card (Y/N): ")
    if card == "N":
        print("Ticket price: £10.00")
    elif card == "Y":
        print("Ticket price: £8.00")
    else:
        print("Invalid input")
elif age > 64:
    print("Ticket price: £6.00")