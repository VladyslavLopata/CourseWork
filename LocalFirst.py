'''
Local search algorithm
'''
def local_first(_list=[], n = 10, m = 3, verbose=False):
	
	#Calculating initial SPT
	import SPT
	matrix = SPT.SPT(_list, n, m, verbose)

	#Reversing each row of matrix
	for i in range(m):
		matrix[i].reverse()

	#Length of the shortest matrix row(last is always shortest for SPT)
	_length = len(matrix[-1])

	#Operating with ordering levels(ukr: rivni vporiadkovanosti)
	#Swap each min-max pair on current ordering level, while there still unswapped elements
	for i in range(_length):
		start_iterator = 0
		end_iterator = m-1

		while start_iterator < end_iterator:
			if _swap_calculate(matrix, start_iterator, i, end_iterator, i):
				_matrix_swap(matrix, start_iterator, i, end_iterator, i)
			start_iterator += 1
			end_iterator -= 1

	#Reverse matrix rows to their previous order
	for i in range(m):
		matrix[i].reverse()

	#CMD output on demand
	if verbose:
		print("Optimised output:")
		for i in range(m):
			print("{}: {}".format(i+1, matrix[i]))

	return matrix
		
	
	 
'''
Helper function to decide whether swap is needed

Tries to swap matrix elements and recalculates target function.
'''
def _swap_calculate(_matrix, row1, column1, row2, column2):
	matrix = []
	for i in range(len(_matrix)):
		matrix.append(_matrix[i].copy())

	C1 = sum(matrix[row1])
	C2 = sum(matrix[row2])

	_matrix_swap(matrix, row1, column1, row2, column2)

	C1_new = sum(matrix[row1])
	C2_new = sum(matrix[row2])

	if abs(C1-C2) > abs(C1_new-C2_new):
		return True
	return False

'''
Helper function to swap matrix elements
'''
def _matrix_swap(_matrix, row1, column1, row2, column2):
	_matrix[row1][column1], _matrix[row2][column2] = _matrix[row2][column2], _matrix[row1][column1]