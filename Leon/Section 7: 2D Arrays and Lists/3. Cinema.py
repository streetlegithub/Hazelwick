# initialise plan, set the seats total
plan = []
seats = 8
# set all seats on every row to 0
for row in range(5):
    plan.append([0] * seats)
print("   1 2 3 4 5 6 7 8")
# remove characters from list output
for row in range(5):
    temp_string = f"{row+1}  {plan[row]}"
    print(temp_string.replace("[", "").replace("]",
          "").replace(",", "").replace("'", ""))
selected_row = ""
selected_seat = ""
# check if its 0 (end condition)
while selected_row != 0:
    selected_row = int(input("Enter a row 1-5: "))
    if selected_row != 0:
        selected_seat = int(input("Enter a seat 1-8: "))
# make sure in range
        if selected_row-1 in range(5):
            if selected_seat-1 in range(8):
# check if taken
                if plan[selected_row-1][selected_seat-1] == "X":
                    print("Seat taken, please select another")
                else:
# set seat as taken and print table again
                    plan[selected_row-1][selected_seat-1] = "X"
                    print("   1 2 3 4 5 6 7 8")
                    for row in range(5):
                        temp_string = f"{row+1}  {plan[row]}"
                        print(temp_string.replace("[", "").replace(
                            "]", "").replace(",", "").replace("'", ""))
# error handling
            else:
                print("Seat needs to be in range 1-8")
        else:
            print("Row needs to be in range 1-5")
total = 0
# calculate total
for row in range(5):
    for seats in range(8):
        if plan[row][seats] == "X":
            total = total
        else:
            total = total + 1
# print remaining seats
print(f"Remaining seats: {total}")
