def balancedSums(arr):
    # Write your code here
    right = sum(arr)
    left = 0
    for i in arr:
        right -= i
        if left == right:
            return "YES"
        left += i
        
    return "NO"