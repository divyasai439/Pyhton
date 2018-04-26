matrix=[[1,2,3], [4,5,6], [7,8,9]]
transpose = []
for i in range(3):
    transposed_rows = []
    for row in matrix:
	    transposed_rows.append(row[i])
    transpose.append(transposed_rows)
print(transpose)