"""
Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
column are set to 0.
"""
import numpy as np


def clear_matrix_at(matrix, i, j):
    matrix[i, :] = 0
    matrix[:, j] = 0


def zero_matrix(matrix: np.ndarray):
    visited_rows = set()
    n_row, n_col = matrix.shape
    for i in range(n_row):
        for j in range(n_col):
            if matrix[i, j] == 0 and i not in visited_rows and j not in visited_rows:
                clear_matrix_at(matrix, i, j)
                visited_rows.add(i)
                visited_rows.add(j)


if __name__ == '__main__':
    mat = np.array([[0, 1, 1, 1], [2, 0, 2, 2], [3, 3, 3, 3], [4, 4, 4, 0]])
    zero_matrix(mat)
    print(mat)