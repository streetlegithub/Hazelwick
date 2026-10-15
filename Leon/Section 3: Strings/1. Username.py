# get user's name
fName = input("First name: ")
lName = input("Last name: ")

# get miscellaneous info
initial = fName[0]
part2 = lName[0:4]
length = len(fName)+len(lName)

# generate username and print result
username = (initial + part2 + str(length)).lower()

print(f"Username: {username}")
