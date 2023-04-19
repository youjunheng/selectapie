# 辅助，判定覆盖矩阵是否满足条件
import numpy as np

# if k is superset of s then 0, else 1 (for convenient of Hadamard product)
def superset_check(k, s):
    if k.issuperset(s):
        return 0
    else:
        return 1

# use K-set and S-set to generate a matrix
# 生成覆盖矩阵
def cover_matrix(k_set, s_set):
    row = len(k_set)
    col = len(s_set)
    matrix = np.zeros((row, col))

    for i in range(row):
        for j in range(col):
            matrix[i][j] = superset_check(k_set[i], s_set[j])
    return matrix

# given a matrix, check if its every row's hadamard product is 0
# 判定覆盖矩阵是否全0
def check_hadamard(matrix):
    result = np.ones((1, matrix.shape[1]))

    # calculate the hadamard product of every line
    for i in range(matrix.shape[0]):
        result = np.multiply(result, matrix[i])
    
    # return result
    
    # if the result is 0, then return True
    if np.count_nonzero(result) == 0:
        return True
    else:
        return False

# test function
def test():
    k_set = [set([1, 2, 3]), set([2, 3, 4]), set([3, 4, 5])]
    s_set = [set([1, 2]), set([2, 3]), set([3, 4]), set([4, 5])]
    matrix = cover_matrix(k_set, s_set)
    print(matrix)
    print(check_hadamard(matrix))
    matrix = np.matrix([[1, 0, 1, 0], 
                        [0, 1, 1, 1], 
                        [1, 0, 1, 0]])
    print(check_hadamard(matrix))

if __name__ == "__main__":
    test()