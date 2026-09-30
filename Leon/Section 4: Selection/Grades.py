mark = int(input("Enter the test mark (0-100): "))

if mark < 0 or mark > 100:
    print("Invalid mark")
elif mark > 70:
    print("A")
elif mark > 60:
    print("B")
elif mark > 50:
    print("C")
elif mark > 40:
    print("D")
elif mark < 40:
    print("U")
else:
    print("Invalid input")
