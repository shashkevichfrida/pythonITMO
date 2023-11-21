import numpy as np
from collections import OrderedDict
def dominant_strategy(matrix):
    matrix = remove_identical_lines(matrix)
    matrix = np.transpose(matrix)

    matrix = remove_identical_lines(matrix)
    matrix = np.transpose(matrix)
    matrix = check_dominant_lines(matrix)

    matrix = np.transpose(matrix)

    matrix = check_dominant_columns(matrix)
    matrix = np.transpose(matrix)
    print(matrix)


def remove_identical_lines(matrix):
    unique_rows_set = OrderedDict.fromkeys(tuple(row) for row in matrix)
    unique_matrix = [list(row) for row in unique_rows_set]
    return unique_matrix


def check_dominant_lines(matrix):
    submis = 0
    stroki_for_del = []
    for i in range(0, len(matrix)):
        for k in range(0, len(matrix)):
            if k!= i:
                for j in range(0, len(matrix[i])):
                    if matrix[i][j] <= matrix[k][j]:
                        submis+=1
                if submis == len(matrix[i]):
                    stroki_for_del.append(i)
                submis = 0
    matrix = np.delete(matrix, stroki_for_del, axis=0)
    return matrix

def check_dominant_columns(matrix):
    submis = 0
    stroki_for_del = []
    for i in range(0, len(matrix)):
        for k in range(0, len(matrix)):
            if k!= i:
                for j in range(0, len(matrix[i])):
                    if matrix[i][j] >= matrix[k][j]:
                        submis+=1
                if submis == len(matrix[i]):
                    stroki_for_del.append(i)
                submis = 0
    matrix = np.delete(matrix, stroki_for_del, axis=0)
    return matrix




