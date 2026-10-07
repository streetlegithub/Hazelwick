# create 2d list with every seat free (0)
# display seating plan with row and seat numbers (1 represents user)
# repeats asks for row and seat until 0 is entered
# validate its a row and seat, refuse booked seats, mark booked seats with X
# output number of free seats left
# 5 rows, 8 seats each
plan = []
seats = 8
for row in range(5):
    plan.append([0] * seats)
print("   1  2  3  4  5  6  7  8")
for row in range(5):
    print(row+1, plan[row])
selectedrow = ""
selectedseat = ""
while selectedrow != 0:
    selectedrow = int(input("Enter a row 1-5: "))
    if selectedrow != 0:
        selectedseat = int(input("Enter a seat 1-8: "))
        if selectedrow-1 in range(5):
            if selectedseat-1 in range(8):
                print("Success")
            else:
                print("Seat needs to be in range 1-8")
        else:
            print("Row needs to be in range 1-5")