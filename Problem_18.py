# Randomly generate a 4-digit number. 
# Ask the user to guess a 4-digit number. 
# For every digit that the user guessed correctly in the correct place, they have a “cow”. 
# For every digit the user guessed correctly in the wrong place is a “bull.” 
# Every time the user makes a guess, tell them how many “cows” and “bulls” they have. 
# Once the user guesses the correct number, the game is over. 
# Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.

import random

def generate_number():
    while True:
        number = random.randint(1000,9999)
        if len(set(str(number))) == 4:
            return number
        
def get_guess():
    while True:
        try:
            guess = int(input("Enter your guess (4-digit number): "))
            if guess < 1000 or guess > 9999:
                raise ValueError
            return guess
        except ValueError:
            print("Invalid guess. Please enter a 4-digit number.")

def check_guess(number, guess):
    cows = 0
    bulls = 0
    number_str = str(number)
    guess_str = str(guess)
    for i in range(4):
        if number_str[i] == guess_str[i]:
            cows += 1
        elif guess_str[i] in number_str:
            bulls += 1
    return cows, bulls

number = generate_number()
num_guesses = 0
print("Guess the 4-digit number (no duplicate digits). ")

while True:
    guess = get_guess()
    num_guesses += 1
    cows, bulls = check_guess(number, guess)

    print(f"You have {cows} cows and {bulls} bulls.")

    if cows == 4:
        print(f"Congratulations! You guesseed the number in {num_guesses} guesses.")
        break