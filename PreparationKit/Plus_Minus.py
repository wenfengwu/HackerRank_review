def plusMinus(arr):
    # Write your code here
    positive = 0
    negative = 0
    zero = 0
    n = len(arr)
    
    for i in arr:
        if i > 0:
            positive += 1
        elif i < 0:
            negative += 1
        else:
            zero += 1
    
    print("{:.6f}".format(positive/n))
    print("{:.6f}".format(negative/n))
    print("{:.6f}".format(zero/n))
