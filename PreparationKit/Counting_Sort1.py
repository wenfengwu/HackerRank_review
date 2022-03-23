# Note
# For this exercise, always return a frequency array with 100 elements. The example above shows only the first 4 elements, the remainder being zeros.

# Challenge
# Given a list of integers, count and return the number of times each value appears as an array of integers.

# Function Description

# Complete the countingSort function in the editor below.

# countingSort has the following parameter(s):

# arr[n]: an array of integers
# Returns

# int[100]: a frequency array

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    # Write your code here
    newArr = [0] * 100
    for i in arr:
        newArr[i] += 1
    return newArr
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
