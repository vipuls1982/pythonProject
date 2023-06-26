#new
import fileinput

import main
import string

file_nation=open("C:\data/nation.csv" , "r")

Lines = file_nation.readlines()

print(Lines)

count = 0
# Strips the newline character
for line in Lines:
 count += 1
 print("Line{}: {}".format(count, line.strip()))