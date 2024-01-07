#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
    else:
        for submatrix in matrix:
            for a, n in enumerate(submatrix):
                print("{:d}".format(n), end="")
                if (a != len(submatrix) - 1):
                    print(" ", end="")
            print()
