# Time for some fake graphics! Let’s say we want to draw game boards that look like this:
#  --- --- --- 
# |   |   |   | 
#  --- --- ---  
# |   |   |   | 
#  --- --- ---  
# |   |   |   | 
#  --- --- --- 
# This one is 3x3 (like in tic tac toe). Obviously, they come in many other sizes (8x8 for chess, 19x19 for Go, and many more).

def print_board():
    print(" --- --- ---")
    print("|   |   |   |")
    print(" --- --- ---")
    print("|   |   |   |")
    print(" --- --- ---")
    print("|   |   |   |")
    print(" --- --- ---")

print_board()
