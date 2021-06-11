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
def isPlaced(i, q, w):
    currentIndex = w.index(i)
    finalIndex = q.index(i)
    print("currentIndex: " + str(currentIndex))
    print("findalIndex: " + str(finalIndex))
    if currentIndex == finalIndex:
        return True
    else:
        print("returning False")
        return False

#def isPlaced(i, q, w):
#    if q.index(i) == w.index(i): # if current index equals final index
#        return True
#    else:
#        return False        
        
#def bribe(i, w):
#    print("bribe: " + str(i))
#    temp = w[w.index(i-1)]
#    w[i-1] = w[i]
#    w[i] = temp
#    print("end bribe")
    
def bribe(n, w):
    i = w.index(n)
    temp = w[i-1]
    w[i-1] = w[i]
    w[i] = temp
    return w
    
def minimumBribes(q):
    # Write your code here
    w = list(range(1, len(q)+1))
    bribesTotal = 0
    bribesLocal = 0
    tooChaotic = False
    for i in list(range(0, len(q)-1)):
        bribesLocal = 0
        while(q[i] != w[i]):
            #print("i: " + str(i) + " q[i]: " + str(q[i]) + " w[i]: " + str(w[i]))
            w  = bribe(q[i], w)
            bribesTotal += 1
            bribesLocal += 1
            #print("new w: " + str(w))
        if bribesLocal > 2:
            tooChaotic = True
            print("Too chaotic")
            break
     
    if tooChaotic == False:
        print(bribesTotal)
    
if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)

