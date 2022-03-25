import math
import os
import random
import re
import sys
from heapq import heapify, heappush, heappop

#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#

def cookies(k, A):
    # Write your code here
    result = 0
    #solve this problem by using heap
    heapify(A)
    while True:
        #get the min value from heap
        last = heappop(A)
        #base case, check min if it is greater the k
        if last >= k:
            return result
        
        if A:
            secondLast = heappop(A)
            #calculate
            temp = last + secondLast * 2
            #push temp to heap
            heappush(A, temp)
            result += 1
        else:
            return -1
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
