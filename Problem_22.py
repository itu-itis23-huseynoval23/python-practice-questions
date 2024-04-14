# Given a .txt file that has a list of a bunch of names, count how many of each name there are in the file, 
# and print out the results to the screen.

with open('filename.txt') as f:
    line = f.readline()
    while line:
        print(line)
        line = f.readline()