# Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number. 
# The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.

def is_number_in_list(ordered_list, number):
    # Check if the number is in the list using binary search
    low = 0
    high = len(ordered_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if ordered_list[mid] == number:
            return True
        elif ordered_list[mid] < number:
            low = mid + 1
        else:
            high = mid - 1
    return False

# Example usage:
ordered_numbers = [1, 2, 5, 7, 8, 11, 13, 20]
number_to_check = 7
result = is_number_in_list(ordered_numbers, number_to_check)
print(result)  # Output: True
