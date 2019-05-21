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


'''
Helper function to evaluate the first TF
'''
def target_C_macron(matrix):
	
	n = 0
	for i in range(len(matrix)):
		n+=len(matrix[i])

	sum = 0

	for j in range(len(matrix)):
		for k in range(len(matrix[j])):
			sum += (len(matrix[j])-k)*matrix[j][k]

	return (sum/n)

'''
Helper function to evaluate the second TF
'''
def target_C_max(matrix):
	sums = []
	for j in range(len(matrix)):
		sums.append(sum(matrix[j]))
	return max(sums)

'''
Generates random task for algorithms
'''
def generate_random_case():

	import random as r
	_work_size=100
	_size = 10
	m = 3
	_list = []
	for i in range(_size):
		_list.append(r.randint(0, _work_size))

	return _list, m, _size

def try_all_in_radius(matrix, row, m):

	#list of swap valuability
	#contains indexes of works to swap and difference between current and new TF
	estimations = []

	#check all possible swaps within the range
	for i in range(m):
		for j in range(row, row+2):
			for k in range(m):
				for f in range(row, row+2):
					if not (j == len(matrix[i]) or f == len(matrix[k])):
						estimations.append([(i,j,k,f), radial_swap_calculate(matrix, i, j, k, f)]) #memorize estimation

	#find the smallest estimation value
	minimal_estimated = 1000000, (0,0,0,0)
	for estimation in estimations:
		if estimation[1][0] <= 0 and estimation[1][1] <= 0:
			if estimation[1][1] < minimal_estimated[0]:
				minimal_estimated = estimation[1][1], estimation[0]
	matrix_swap(matrix, minimal_estimated[1][0], minimal_estimated[1][1], minimal_estimated[1][2], minimal_estimated[1][3]) #swap