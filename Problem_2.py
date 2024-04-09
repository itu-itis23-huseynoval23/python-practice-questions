# Ask the user for a number. 
# Depending on whether the number is even or odd, 
# print out an appropriate message to the user.
# Hint: how does an even / odd number react differently when divided by 2?

num = input("Enter a number: ")
rem = int(num) % 2
if rem > 0:
    print("Your number is odd.")
else:
    print("Your number is even.")