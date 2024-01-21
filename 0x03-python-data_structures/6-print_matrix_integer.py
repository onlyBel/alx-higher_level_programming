#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for i in matrix:
            for b in i:
                print("{:d}".format(b), end=' 'if b != i[-1] else '')
            print()
