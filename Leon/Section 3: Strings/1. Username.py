fName=input("First name: ")
lName=input("Last name: ")

initial = fName[0]
part2 = lName[0:4]
length = len(fName)+len(lName)

username = (initial + part2 + str(length)).lower()

print(f"Username: {username}")