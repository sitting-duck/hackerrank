#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#
def check(index, c):
    result = [False, False]
    print("c[index+1]: " + str(c[index+1]))
    if c[index+1] == 0:
        result[0] = True
    else:
        result[0] = False
    
    if index+2 <= len(c) - 1 and c[index+2] == 0:
        result[1] = True
    else:
        result[1] = False
    return result        
    
def jumpingOnClouds(c):
    
    currentCloudIndex = 0
    numHop = 0
    while currentCloudIndex < len(c) - 1:
        result = check(currentCloudIndex, c)
        print("result: " + str(result))
        if result[1]:
            currentCloudIndex += 2
        else:
            currentCloudIndex += 1
        numHop += 1
        print("currentCloudIndex: " + str(currentCloudIndex))
    return numHop
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()

