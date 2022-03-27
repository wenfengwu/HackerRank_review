def pangrams(s):
    # Write your code here
    result = set(s.replace(' ', '').lower())
    return 'pangram' if len(result) == 26 else 'not pangram'