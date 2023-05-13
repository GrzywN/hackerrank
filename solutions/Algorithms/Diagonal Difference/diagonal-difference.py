#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    matrix_len = len(arr)

    left_diagonal_elements = []
    right_diagonal_elements = []

    for i in range(matrix_len):
        left_diagonal_elements.append(arr[i][i])
        right_diagonal_elements.append(arr[i][matrix_len - 1 - i])

    difference = abs( sum(left_diagonal_elements) - sum(right_diagonal_elements) )

    return difference


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
