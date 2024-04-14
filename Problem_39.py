# Print out a message addressed to them that tells them the year 
# that they will turn 100 years old), except don’t explicitly write out the year.

import datetime

current_year = datetime.datetime.now().year
print(current_year)
name = input("What is your name? ")
age = int(input("How old are you? "))
print(f"{name}, you will be 100 years old in {current_year - age + 100}")