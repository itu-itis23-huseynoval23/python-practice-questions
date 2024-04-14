import json

# Load the birthday dictionary from the JSON file
with open('birthdays.json', 'r') as file:
    birthdays = json.load(file)

print('Welcome to the birthday dictionary. We know the birthdays of:')
for name in birthdays:
    print(name)

print('Whose birthday do you want to look up?')
name = input()

if name in birthdays:
    print('{}\'s birthday is {}.'.format(name, birthdays[name]))
else:
    print('Sadly, we don\'t have {}\'s birthday.'.format(name))
