#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
#    if not matrix:
#       return None
    for vert in matrix:
        for i in range(len(vert)):
            print("{:d}".format(vert[i],
                  end="" if colomn == len((vert) - 1) else " "))
        print("")
