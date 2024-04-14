# The player guesses one letter at a time until the entire word has been guessed.

import random

# Read all the list of words
words = []
with open('sowpods.txt', 'r') as f:
    line = f.readline().strip()
    words.append(line)
    while line:
        line = f.readline().strip()
        words.append(line)

# Generate a random number
random_index = random.randint(0, len(words))

# Select a random word
secret_word = words[random_index].upper()
word_length = len(secret_word)
guessed_letters = set()
correct_guesses = set()

print("Welcome to Hangman!")
print("_ " * word_length)  # Display underscores for each letter in the word

def display_word():
    displayed_word = ""
    for letter in secret_word:
        if letter in correct_guesses:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "
    return displayed_word.strip()

while True:
    guess = input("Guess your letter: ").upper()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabetic letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.add(guess)

    if guess in secret_word:
        correct_guesses.add(guess)
        print(display_word())
    else:
        print("Incorrect!")

    if len(correct_guesses) == len(set(secret_word)):
        print("Congratulations! You guessed the word:", secret_word)
        break
