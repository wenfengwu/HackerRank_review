# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with  places after the decimal.

# Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to  are acceptable.

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
    # Write your code here
    positive, negative, zero = 0, 0, 0
    for i in arr:
        if i == 0:
            zero += 1
        elif i > 0:
            positive += 1
        else:
            negative += 1
    print(format(positive/len(arr), '.6f'))
    print(format(negative/len(arr), '.6f'))
    print(format(zero/len(arr), '.6f'))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
