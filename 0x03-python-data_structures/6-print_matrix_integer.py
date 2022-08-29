#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        if len(row) == 0:
            print ()
        for colomn in range(len(row)):
            print("{:d}".format(row[colomn],
                end="" if colomn == len((row) - 1) else " ")
        print("")   
