seconds = int(input("Enter number of seconds: "))
print(f"{seconds} seconds is {seconds//3600} hour(s), {(seconds%3600)//60} minute(s) and {((seconds%3600)%60)} second(s).")