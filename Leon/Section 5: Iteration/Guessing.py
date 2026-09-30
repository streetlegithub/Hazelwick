import random
count = 1
guess = int(input("Guess my number (1-100): "))
number=random.randint(1,100)

while guess != number:
    if guess > number:
        print("Too high!")
    elif guess < number:
        print("Too low!")
    count=count+1
    guess=int(input("Guess my number (1-100): "))

print(f"Correct! You took {count} guesses!")