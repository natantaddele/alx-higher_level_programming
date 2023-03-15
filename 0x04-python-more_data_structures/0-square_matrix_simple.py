#!/usr/bin/python3
def square_matrix_simple(matrix):
    output_matrix = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[i])):
            row.append(matrix[i][j] ** 2)
        output_matrix.append(row)
    return output_matrix
