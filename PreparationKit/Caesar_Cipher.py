#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    answer = ""
    for i in s:
        if i.islower():
            # a -> 97
            answer += chr((ord(i)-97+k) % 26 + 97)
        elif i.isupper():
            # A -> 65
            answer += chr((ord(i) -65+k) %26 + 65)
        else:
            answer += i
    
    return answer