names = ["Leon","Oliver","Raahil","Yog","Mr Luis","Mr Soni","Mohammed","Hrushikesh"]
name = input("Enter a name to find: ")
for i in range(8):
    if names[i] == name:
        print(f"{name} found at position {i+1}")