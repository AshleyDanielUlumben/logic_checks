# 1461. Check If a String Contains All Binary Codes of Size K
def hasAllCodes( s: str, k: int) -> bool:
    # Important
    # Sliding Window technique
    # window size = k
    subStr = set() # Hashset so we dont get duplicates in the set

    # Verifying each sub-string 
    # capturing a window of size k
    for i in range(len(s) - k + 1):  # why minus k
        subStr.add(s[i:i+k])

    return (len(subStr) == 2**k)

            
s = '00110110'
k = 2
print(hasAllCodes(s,k))
          