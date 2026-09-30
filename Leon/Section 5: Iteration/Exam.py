count=1
lowmark = 0
highmark = 0
total = 0
mark = int(input("Enter mark ('-1' to finish): "))
if mark > 100 or mark < 0:
    lowmark = mark
    highmark = mark

while mark != -1:
    int(input("Enter mark ('-1' to finish): "))
    if mark > 100 or mark < 0:
        if lowmark > mark:
            lowmark = mark
        elif highmark < mark:
            highmark = mark
        count = count+1
        total = total + mark
    else:
        print("Invalid — 0-100")
print(f"Total: {total}")
