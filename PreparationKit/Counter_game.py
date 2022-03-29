def counterGame(n):
    # Write your code here
    result = bin(n-1).count('1')
    if result % 2 != 0:
        return 'Louise'
    else:
        return 'Richard'