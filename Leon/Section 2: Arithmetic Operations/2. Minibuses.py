# capacity of minibus as constant
CAPACITY = 16
# calculate minibuses and spare students
students = int(input("How many students are going on the trip? "))
print(
    f"Full minibuses: {students//CAPACITY}\nStudents left over: {students % CAPACITY}")
