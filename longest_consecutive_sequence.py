# Longest Consecutive Sequence

def longConsecSeq(nums):
    longest = 0     # Indicates the Longest sequence
    seqSet = set(nums)

    # The begining of a seq can be identified by checking if it has a value before it
    for n in nums:
        if (n - 1) not in seqSet:        
            length = 0
            while (n + length) in seqSet:
                length += 1
            longest = max(length, longest)        
    
    return longest


seqlist = [100, 4, 200, 1, 3, 2,5,6]
print(longConsecSeq(seqlist))

# Expected Output -> 4 
# Explanation -> (1, 2, 3, 4) is the longest sequence