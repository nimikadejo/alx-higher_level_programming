#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    New_matrix = []
    for row in matrix:
        funct = list(map(lambda x: x**2, row))
        New_matrix.append(funct)
    return New_matrix
