temperature = []
total = 0
highest = 0
count = 0

for i in range(5):
    temperature.append(float(input(f"Enter temperature {i+1}: ")))
    total = temperature[i] + total
    if highest <= temperature[i]:
        highest = temperature[i]
average = (total/len(temperature))
for i in range(5):
    if temperature[i] > average:
        count = count+1
print(
    f"Temperatures: {temperature}\nAverage: {average}\nHighest: {highest}\nDays above average: {count}")