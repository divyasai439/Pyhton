#bin/usr

# Basic case

import os

clear=lambda:os.system('cls')
clear()

squares=[]
for x in range(10):
     squares.append(x ** 2)
print(squares)
print(x)

# equivalently
squares1=[(x ** 2) for x in range(10)]
print(squares1)
print(x)

#equivalently 

squares2=list(map(lambda x: x **2, range(10)))
print(squares2)
print(x)

#  listcomp combines the elements of two lists if they are not equal:

print([(x,y) for x in [1,2,3] for y in [3,4,1] if x!=y])

# equivalent to:

combos=[]
for x in [1,2,3]:
    for y in [3,4,1]:
	    if x!=y:
		    combos.append((x,y))
print(combos)

# Nested List Comprehensions-- matrix 

matrix=[[1,2,3], [4,5,6], [7,8,9]]

# transpose rows and columns

print([[row[i] for row in matrix] for i in range(3)])

# equivalent to

transpose = []
for i in range(3):
    transposed_rows = []
    for row in matrix:
	    transposed_rows.append(row[i])
    transpose.append(transposed_rows)
print(transpose)

# equivalent to

transposed= []
for i in range(3):
    transposed.append([row[i] for row in matrix])
print(transposed)
