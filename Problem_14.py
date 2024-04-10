# Write a program (function!) that takes a list and returns a new list that 
# contains all the elements of the first list minus all the duplicates.

def remove_duplicates(list):
    unique = []
    for element in list:
        if element not in unique:
            unique.append(element)
    return unique

num_element = int(input("Enter the number of elements: "))
list = []

for i in range(num_element):
    num = int(input(f"Enter element {i+1}: "))
    list.append(num)

new_list = remove_duplicates(list)

print("Original list: ", list)
print("List without duplicates: ", new_list)




