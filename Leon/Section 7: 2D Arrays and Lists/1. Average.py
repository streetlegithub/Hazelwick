# hardcoded names+scores
names = ["Bob", "Steve", "John"]

scores = [[65, 72, 58, 80], [90, 85, 88, 92], [45, 60, 52, 49]]

# get the average scores
for row in range(len(scores)):
    total = 0
    for col in range(len(scores[row])):
        total = total+scores[row][col]
    average = total/len(scores[row])
    print(f"{names[row]}: total = {total}, average = {average}")

# 
for col in range(len(scores[0])):
    total = 0
    for row in range(len(scores)):
        total = total+scores[row][col]
    print(f"Test {col+1} average: {round((total/len(scores)), 1)}")
