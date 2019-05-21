#legacy
def _swap_calculate(_matrix, row1, column1, row2, column2):
	matrix = []
	for i in range(len(_matrix)):
		matrix.append(_matrix[i].copy())

	C1 = sum(matrix[row1])
	C2 = sum(matrix[row2])

	matrix_swap(matrix, row1, column1, row2, column2)

	C1_new = sum(matrix[row1])
	C2_new = sum(matrix[row2])

	return abs(C1-C2) - abs(C1_new-C2_new)

'''
Helper function to decide whether swap is needed

Tries to swap matrix elements and recalculates target function.
'''
def radial_swap_calculate(_matrix, row1, column1, row2, column2):
	matrix = []
	for i in range(len(_matrix)):
		matrix.append(_matrix[i].copy())

	CM1 = target_C_macron(matrix)
	Cmax1 = target_C_max(matrix)

	matrix_swap(matrix, row1, column1, row2, column2)

	CM2 = target_C_macron(matrix)
	Cmax2 = target_C_max(matrix)

	return CM2-CM1, Cmax2-Cmax1

'''
Helper function to swap matrix elements
'''
def matrix_swap(_matrix, row1, column1, row2, column2):
	_matrix[row1][column1], _matrix[row2][column2] = _matrix[row2][column2], _matrix[row1][column1]

def target_C_macron(matrix):
	
	n = 0
	for i in range(len(matrix)):
		n+=len(matrix[i])

	sum = 0

	for j in range(len(matrix)):
		for k in range(len(matrix[j])):
			sum += (len(matrix[j])-k)*matrix[j][k]

	return (sum/n)

def target_C_max(matrix):
	sums = []
	for j in range(len(matrix)):
		sums.append(sum(matrix[j]))
	return max(sums)