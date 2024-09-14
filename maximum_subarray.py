# Maximum Subarray
lis = [5,4,-1,7,8]

# Expected Result = 6
# Explanation = [4, -1, 2, 1] -> 4 + (-1) + 2 + 1 = 6

# Seems like a sliding window problem 
def maxSub(nums):
    # Setting the max sum to be the first integer of the list
    maxSum = nums[0]
    # The current sum will be updated frequently
    curSum = 0

    for n in range(0, len(nums)):
        # we dont want to store negative values
        if curSum < 0:
            curSum = 0
        
        # checking the max by adding each integer step by step
        curSum += nums[n]
        maxSum = max(maxSum, curSum)
    
    return maxSum

def maxSubBrute(nums):
    # brute force solution
    for i in range(0, len(nums)):
        for j in range(i, len(nums)):
            res = nums[0]
            currSum = 0
            currSum += nums[j]
        res = max(res, currSum)
    return res

print(maxSub(lis), maxSubBrute(lis))

    

