import numpy as np

# if k is superset of s then 0, else 1 (for convenient of Hadamard product)
def superset_check(k, s):
    if k.issuperset(s):
        return 0
    else:
        return 1

# use K-set and S-set to generate a matrix
def cover_matrix(k_set, s_set):
    row = len(k_set)
    col = len(s_set)
    matrix = np.zeros((row, col))

    for i in range(row):
        for j in range(col):
            matrix[i][j] = superset_check(k_set[i], s_set[j])
    return matrix

# given a matrix, check if its every row's hadamard product is 0
def jls_extract_def(matrix):
    # calculate the hadamard product of every column
    for i in range(matrix.shape[1]):
        column = matrix[:, i] 
        result = np.multiply(column)
    return result


def check_hadamard(matrix):
    result = np.ones(matrix.shape[0], 1)

    result = jls_extract_def(matrix)
    
    # if the result is 0, then return True
    if np.count_nonzero(result) == 0:
        return True
    else:
        return False