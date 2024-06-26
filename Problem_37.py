# This exercise asked you to refactor this code snippet to refactor 
# (taken from a correct but very repeated solution to exercise 24 on this website):

def print_verticals(grid_size):
	vertical_string = "|"
	for i in range(grid_size):
		vertical_string += "   |"
	print(vertical_string)

def print_horizontals(grid_size):
	horiz_string = ""
	for i in range(grid_size):
		horiz_string += " ---"
	print(horiz_string)
	
grid_size_x = 3
grid_size_y = 5
print_horizontals(grid_size_x)
for i in range(grid_size_y):
	print_verticals(grid_size_x)
	print_horizontals(grid_size_x)