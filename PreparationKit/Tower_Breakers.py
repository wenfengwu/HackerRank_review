# Two players are playing a game of Tower Breakers! Player  always moves first, and both players always play optimally.The rules of the game are as follows:

# Initially there are  towers.
# Each tower is of height .
# The players move in alternating turns.
# In each turn, a player can choose a tower of height  and reduce its height to , where  and  evenly divides .
# If the current player is unable to make a move, they lose the game.
# Given the values of  and , determine which player will win. If the first player wins, return . Otherwise, return .

# Example. 

# There are  towers, each  units tall. Player  has a choice of two moves:
# - remove  pieces from a tower to leave  as 
# - remove  pieces to leave 

# Let Player  remove . Now the towers are  and  units tall.

# Player  matches the move. Now the towers are both  units tall.

# Now Player  has only one move.

# Player  removes  pieces leaving . Towers are  and  units tall.
# Player  matches again. Towers are both  unit tall.

# Player  has no move and loses. Return .

# Function Description

# Complete the towerBreakers function in the editor below.

# towerBreakers has the following paramter(s):

# int n: the number of towers
# int m: the height of each tower
# Returns

# int: the winner of the game

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'towerBreakers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def towerBreakers(n, m):
    # Write your code here
    #if m is 1, play 2 win with no doubt
    if m == 1:
        return 2
    #else, we should the number of towers is odd or even, if is odd, always player 1 win, because play 1 can reduce m-1, then make y = 1, so player 2 lose. If tower number is even, and both players always play optimally, which means play2 always follow player1 operation, so player2 win
    else:
        if n % 2 == 1:
            return 1
        else:
            return 2
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = towerBreakers(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
