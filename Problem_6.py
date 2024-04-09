# Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)

num1 = str(input("Please enter a number): "))
num2 = num1[::-1]
if num1 == num2:
    print("Your number is palindrome.")
else:
    print("Your number is not palindrome.")