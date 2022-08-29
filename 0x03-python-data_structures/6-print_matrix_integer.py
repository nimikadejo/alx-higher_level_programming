#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
#    if not matrix:
#        return None
    for vert in matrix:
        if len(vert) == 0:
            print()
        for hori in range(len(vert)):
            print("{:d}".format(vert[hori],
                  end="" if colomn == len((vert) - 1) else " "))
        print("")
