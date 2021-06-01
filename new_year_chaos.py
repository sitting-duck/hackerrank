#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#            
def isSorted(q):
    isSorted = True
    for i in range(0, len(q) - 1):
        #print(" i: " + str(q[i]) + " i+1: " + str(q[i+1]))
        if i < len(q) - 1 and q[i] > q[i+1]:
            return False
    return True

def isTooChaotic(swapped):
    for i in range(0, len(swapped) - 1):
        if swapped[i] > 2:
            return True
    return False    
    
def minimumBribes(q):
    swapped = [0] * n
    numSwapsTotal = 0
    
    while isSorted(q) is False: # if line is sorted we are done
        print("\tisSorted: " + str(isSorted(q)) + " q: " + str(q))
    
        for i in range(0, len(q)-1):
            # if two individuals are out of order maybe they can swap
            outOfOrder = q[i+1] < q[i]
            print("\toutOfOrder: " + str(outOfOrder) + " i: " + str(i) + " q[i]: " + str(q[i]) + " q[i+1]: " + str(q[i+1]))
            
            
            # if two individuals have not already swapped twice, they can swap
            #bothCanSwap = True if (swapped[i] < 2 and swapped[i+1] < 2) else False
            #bothCanSwap = True if (True) else False
            bothCanSwap = True
            if swapped[i] < 2 and swapped[i+1] < 2:
                bothCanSwap = True
            else: 
                bothCanSwap = False
            print("\tbothCanSwap: " + str(bothCanSwap) + " swapped: " + str(swapped))
            
            if outOfOrder and bothCanSwap:
                temp = q[i]   # do
                q[i] = q[i+1] # the 
                q[i+1] = temp # swap
                
                # update swapping state array of who has swapped how many times
                swapped[i] = swapped[i] + 1      # can use +=? 
                swapped[i+1] = swapped[i+1] + 1  # can use +=?
                numSwapsTotal += 1
    
    if isTooChaotic(swapped):
        print("Too Chaotic")
    else: 
        print("numSwapsTotal: " + str(numSwapsTotal) + " q: " + str(q))

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)

