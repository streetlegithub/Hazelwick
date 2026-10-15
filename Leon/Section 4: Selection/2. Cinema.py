# get age from user
age = int(input("Enter your age: "))
# 12 and below get £5, 12-17 get £7
if age <= 12:
    print("Ticket price: £5.00")
elif age < 17 and age > 12:
    print("Ticket price: £7.00")
# 18-64 can possibly get student discount £8, else keep £10
elif age > 18 and age < 64:
    card = input("Student Card (Y/N): ")
    if card == "N":
        print("Ticket price: £10.00")
    elif card == "Y":
        print("Ticket price: £8.00")
# error handling
    else:
        print("Invalid input")
# elderly discount £6
elif age > 64:
    print("Ticket price: £6.00")
