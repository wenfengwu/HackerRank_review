def migratoryBirds(arr):
    # Write your code here
    counter = defaultdict(int)
    for i in arr:
        counter[i] += 1
    result = 0
    maxTime = 0
    for i in range(1,6):
        if counter[i] > maxTime:
            maxTime = counter[i]
            result = i
            
    return result