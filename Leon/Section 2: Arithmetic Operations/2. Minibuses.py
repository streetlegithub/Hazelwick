CAPACITY = 16
students = int(input("How many students are going on the trip? "))
print(f"Full minibuses: {students//CAPACITY}")
print(f"Students left over: {students%CAPACITY}")