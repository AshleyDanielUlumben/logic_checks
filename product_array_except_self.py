# Product of Array except self

# Solving using Prefix and Postfix technique

lis = [1, 2, 3, 4]
# Expected = [24, 12, 8, 6]

def prodArr(nums):
    output = [1] * len(nums)

    prefix = 1
    # prefix = [1, 1x1 =1, 1x2 =2, 2x3 =6]
    # prefix = [1, 1, 2, 6]
    # output = [1, 1, 2, 6]
    for n in range(len(nums)):
        output[n] = prefix 
        prefix *= nums[n]
    #print(output)
    
    postfix = 1
    # postfix calculate in reverse
    # postfix = [1x12x2 = 24, 1x4x3 = 12, 2x1x4 = 8, 6x1 = 6]
    for n in range(len(nums) -1, -1, -1): # Iterate in Reverse
        output[n] *= postfix
        postfix *= nums[n]
    #print(output)
    return output

print(prodArr(lis))



