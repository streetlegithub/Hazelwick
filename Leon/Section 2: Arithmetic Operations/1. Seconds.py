# get seconds from user input
seconds = int(input("Enter a number of seconds: "))
# print hours, minutes, seconds
print(f"{seconds} seconds is {seconds//3600} hour(s), {(seconds % 3600)//60} minute(s) and {((seconds % 3600) % 60)} second(s).")
