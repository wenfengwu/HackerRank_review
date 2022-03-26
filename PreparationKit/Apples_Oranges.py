import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    apple = 0
    orange = 0
    for i in apples:
        if i > 0 and t >= a + i >= s:
            apple += 1
    
    for j in oranges:
        if j < 0 and s<=b + j<= t:
            orange += 1
    print(apple)
    print(orange)