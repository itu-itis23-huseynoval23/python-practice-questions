# Take two lists, say for example these two:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). 
# Make sure your program works on two lists of different sizes.

num_elements1 = int(input("Enter the number of elements in the list a: "))
num_elements2 = int(input("Enter the number of elements in the list b: "))

a = []
b = []

for i in range(num_elements1):
    num = int(input(f"Enter element {i+1} of a: "))
    a.append(num)

for j in range(num_elements2):
    num = int(input(f"Enter element {j+1} of b: "))
    b.append(num)

print(set(a).intersection(set(b)))