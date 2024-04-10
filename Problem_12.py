# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) 
# and makes a new list of only the first and last elements of the given list.

num_element = int(input("Enter the number of elements: "))
a = []

for i in range(num_element):
    num = int(input(f"Enter element {i+1}: "))
    a.append(num)

b = [a[0], a[-1]]
print(b)