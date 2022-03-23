n = "148"
k = 3

def superDigit(n, k):
    # Write your code here
    nums = int(n*k)
    print(nums)
    if 1 <= nums < 10:
        return nums

    while True:
        result = 0
        while nums >= 1:
            result += nums % 10
            nums = nums // 10
        print(result)
        if 1 <= result < 10:
            return result
        else:
            nums = result

superDigit(n,k)