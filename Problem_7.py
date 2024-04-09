# Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
# Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.

num_elements = int(input("Enter the number of elements: "))
a = []

for i in range(num_elements):
    num = int(input(f"Enter element {i+1}: "))
    a.append(num)

b = []

for i in a:
    if i % 2 == 0:
        b.append(i)

print(b)