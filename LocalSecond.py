import Util as u
import SPT

def local_second(_list=[], n = 10, m = 3, verbose=False):

	#Calculating initial SPT
	
	matrix = SPT.SPT(_list, n, m, verbose)

	_length = len(matrix[-1])

	for it in range(n):
		for i in range(_length):
			try_all_in_radius(matrix, i, m)

	#CMD output on demand
	if verbose:
		print("Optimised output:")
		for i in range(m):
			print("{}: {}".format(i+1, matrix[i]))

def try_all_in_radius(matrix, row, m):

	estimations = []
	for i in range(m):
		for j in range(row, row+2):
			for k in range(m):
				for f in range(row, row+2):
					if not (j == len(matrix[i]) or f == len(matrix[k])):
						estimations.append([(i,j,k,f),u.radial_swap_calculate(matrix, i, j, k, f)])

	minimal_estimated = 1000000, (0,0,0,0)
	for estimation in estimations:
		if estimation[1][0] <= 0 and estimation[1][1] <= 0:
			if estimation[1][1] < minimal_estimated[0]:
				minimal_estimated = estimation[1][1], estimation[0]
	u.matrix_swap(matrix, minimal_estimated[1][0], minimal_estimated[1][1], minimal_estimated[1][2], minimal_estimated[1][3])


local_second(n = 15, verbose = True)