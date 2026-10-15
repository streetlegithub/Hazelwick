# initialise all variables, start counter from 0
count = 0
low_mark = 0
high_mark = 0
total = 0
mark = 0
# begin looping until we get the exit condition
while mark != -1:
# ask for marks repeatedly
    mark = int(input("Enter mark ('-1' to finish): "))
# if its the first run, set both the highest and lowest to a base value
    if count == 0:
# always check bounds
        if mark <= 100 and mark >= 0:
            low_mark = mark
            high_mark = mark
        else:
            print("Invalid — 0-100")
# this will repeat, unlike the block above
# check bounds again
    if mark <= 100 and mark >= 0:
# check for lowest, highest marks
        if low_mark > mark:
            low_mark = mark
        elif high_mark < mark:
            high_mark = mark
# increment counter + increase total
        if mark != -1:
            count = count+1
            total = total + mark
# error handling + total printing
    else:
        if mark == -1:
            print(f"Marks entered: {count}\nAverage: {total/count}\nHighest: {high_mark}\nLowest: {low_mark}")
        else: 
            print("Invalid — 0-100")
