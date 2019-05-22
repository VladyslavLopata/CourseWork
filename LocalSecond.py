def local_second(_list=[], n=10, m=3):

    import Util as u
    import SPT

    # initial SPT
    matrix = SPT.SPT(_list, n, m)

    _length = len(matrix[-1])

    # n times try to swap values and recalculate TF. Accept the swaps with best possible TF value
    for _ in range(n):
        for i in range(_length):
            u.try_all_in_radius(matrix, i, m)

    return matrix
