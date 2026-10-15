# get random library
import random
# start count at 1 instead of 0
count = 1
# have the user guess
guess = int(input("Guess my number (1-100): "))
# generate the random number 1-100
number = random.randint(1, 100)
# if they get it wrong
while guess != number:
# is it too high?
    if guess > number:
        print("Too high!")
# or too low?
    elif guess < number:
        print("Too low!")
# increase counter
    count = count+1
# ask for input again
    guess = int(input("Guess my number (1-100): "))
# if guess is correct, while loop ends, print guess counter
print(f"Correct! You took {count} guesses!")
