def SPT(_list=[], n = 10, m = 3, verbose=False):

        
        import random as r
        _work_size=100
        
        _size = n

        #---------------------------list initialization----------------------------#
        if len(_list) == 0:
                _size = 10
                m = 3
                for i in range(_size):
                        _list.append(r.randint(0, _work_size))
        #--------------------------------list sort---------------------------------#
        _list.sort()

        #-----------------------------------spt------------------------------------#
        matrix = []
        for i in range(m):
                matrix.append([])

        j = 0
        for i in range(_size):
                matrix[j].append(_list[i])
                j = (j+1) % m

        #----------------------------------output----------------------------------#
        if verbose:
                print("Initial array:\n{}".format(_list))
                print("SPT-output:")
                for i in range(len(matrix)):
                        print("{}: {}".format(i+1, matrix[i]))
        return matrix
