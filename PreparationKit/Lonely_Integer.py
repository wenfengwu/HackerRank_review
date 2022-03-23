# Given an array of integers, where all elements but one occur twice, find the unique element.

# Function Description

# Complete the lonelyinteger function in the editor below.

# lonelyinteger has the following parameter(s):

# int a[n]: an array of integers
# Returns

# int: the element that occurs only once


import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # Write your code here
    tempDict = {}
    for i in a:
        if i in tempDict:
            tempDict[i] += 1
        else:
            tempDict[i] = 1
            
    for key in tempDict:
        if tempDict[key] == 1:
            return key

#goes with math way:
def lonelyinteger(a):
    return 2*sum(set(a)) - sum(a)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()