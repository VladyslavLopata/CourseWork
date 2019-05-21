'''
Local search algorithm
'''
def local_first(_list=[], n = 10, m = 3, verbose=False):
	
	import Util as u

	#Calculating initial SPT
	import SPT
	matrix = SPT.SPT(_list, n, m, False)

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
			if u.radial_swap_calculate(matrix, start_iterator, i, end_iterator, i)[1] < 0:
				u.matrix_swap(matrix, start_iterator, i, end_iterator, i)
			start_iterator += 1
			end_iterator -= 1

	#Reverse matrix rows to their previous order
	for i in range(m):
		matrix[i].reverse()

	#CMD output on demand
	if verbose:
		print("Optimised via local 1:")
		for i in range(m):
			print("{}: {}".format(i+1, matrix[i]))

	return matrix
