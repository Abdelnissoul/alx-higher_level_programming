#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
    else:
        for sub in range(len(matrix)):
            if elem != len(matrix[sub]) - 1:
                closing = ' '
            else:
                closing = ''
            print("{:d}".format(matrix[sub][elem]), end=closing)
        print()
