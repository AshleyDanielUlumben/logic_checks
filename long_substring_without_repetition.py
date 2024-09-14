# Longest Substring without repeating characters

str1 = "pwwkew"

def Lswrc(s):
    # Got to return the len of the longest substring
    # Using the sliding window technique
    # and pointer
    
    charSet = set()
    res = 0

    l = 0
    for r in range(len(s)):

        while s[r] in charSet:
            charSet.remove(s[l])
            l += 1            

        charSet.add(s[r])

        # why (r - l + 1) --> because len of the sliding window         
        # The plus 1 is tripping me off
        res  = max(res, r - l + 1)
    
    return res

print(Lswrc(str1))