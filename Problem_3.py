# Take a list, say for example this one:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.

# Ask for the number of elements in the list
num_elements = int(input("Enter the number of elements in the list: "))

# Initialize an empty list to store the elements
a = []

# Get the elements from the user
for i in range(num_elements):
    num = int(input(f"Enter element {i+1}: "))
    a.append(num)

# Print elements less than 5
result = [num for num in a if num < 5]
print("Elements less than 5:", result)
