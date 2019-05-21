def SPT(_list=[], n = 10, m = 3):

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

	return matrix
