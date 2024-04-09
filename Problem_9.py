# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.

import random
random_number = random.randint(1, 9)

while True:
    user_guess = int(input("Guess the number between 1 and 9: "))

    if user_guess < random_number: 
        print("Your answer is low! Try again.")
    elif user_guess > random_number:
        print("Your answer is high! Try again.")
    else:
        print("Congratulations! You guessed it right.")
        break
