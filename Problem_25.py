# This time, we’re going to do exactly the opposite. 
# You, the user, will have in your head a number between 0 and 100. 
# The program will guess a number, and you, the user, will say whether 
# it is too high, too low, or your number.

def guess_number():
    low = 0
    high = 100

    while True:
        guess = (low + high) // 2
        print(f"Is your number {guess}?")
        response = input("Enter 'h' if the guess is too high, 'l' if too low, or 'c' if correct: ")

        if response == 'c':
            print("Great! I guessed your number.")
            break
        elif response == 'h':
            high = guess - 1
        elif response == 'l':
            low = guess + 1
        else:
            print("Invalid input. Please enter 'h', 'l', or 'c'.")

guess_number()
