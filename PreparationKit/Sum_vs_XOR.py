def sumXor(n):
    # Write your code here
    if n == 0:
        return 1
    result = bin(n).count('0')
    if result < 1:
        return 0
    else:
        return 2**(result - 1)