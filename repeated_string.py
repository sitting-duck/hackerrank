#!/bin/python3

import math
import os
import random
import re
import sys
import unittest

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def createRepeatedString_too_slow(s, n):
    newString = ""
    print("s: " + str(s))
    while len(newString) + len(s) < n:
        newString += s
        print("str: " + newString)
    index = 0
    while len(newString) < n:
        newString += s[index]
        index += 1
    print("newString: " + newString)
    return newString

def createRepeatedString(s, n):
    numRepeat = n // len(s)
    print("numRepeat: " + str(numRepeat))
    #repeatedString = s * numRepeat
    for i in irange(numRepeat):
        repeatedString += s    
    
    repeatedString += s[0:n - numRepeat*len(s)]
    print("repeatedString: " + repeatedString)
    return repeatedString
    
def repeatedString(s, n):    
    #return createRepeatedString(s, n).count('a')
    L = len(s)
    first = s.count('a') * (n//L)
    second = s[:n % L].count('a')
    print("first: " + str(first))
    print("second: " + str(second))
    print(s.count('a') * (n//L) + s[:n % L].count('a'))
    return first + second
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()

