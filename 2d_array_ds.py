#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def sumHourGlass(x, y, arr):
    sum = arr[y][x]
    sum += arr[y][x+1]
    sum += arr[y][x+2]
    sum += arr[y+1][x+1]
    sum += arr[y+2][x]
    sum += arr[y+2][x+1]
    sum += arr[y+2][x+2]
    return sum

def hourglassSum(arr):
    highest = 0
    for x in range(0, 4):
        for y in range(0, 4):
            current = sumHourGlass(x, y, arr)
            if current > highest:
                highest = current
    return highest                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

