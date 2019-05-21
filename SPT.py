def SPT(_list=[], n = 10, m = 3, verbose=False):

	#--------------------------------list sort---------------------------------#
	_list.sort()

	#-----------------------------------spt------------------------------------#
	matrix = []
	for i in range(m):
		matrix.append([])

	j = 0
	for i in range(n):
		matrix[j].append(_list[i])
		j = (j+1) % m

	#----------------------------------output----------------------------------#
	if verbose:
		print("Initial array:\n{}".format(_list))
		print("SPT-output:")
		for i in range(len(matrix)):
			print("{}: {}".format(i+1, matrix[i]))
	return matrix
