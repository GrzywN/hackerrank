#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    plus_count = 0
    minus_count = 0
    zero_count = 0

    for num in arr:
        if num > 0:
            plus_count += 1
        elif num < 0:
            minus_count += 1
        else:
            zero_count += 1

    plus_ratio = round(plus_count / len(arr), 6)
    minus_ratio = round(minus_count / len(arr), 6)
    zero_ratio = round(zero_count / len(arr), 6)

    print(plus_ratio)
    print(minus_ratio)
    print(zero_ratio)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
