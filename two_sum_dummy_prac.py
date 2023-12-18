# 2Sum Program

#nums = [2,5,7,11,15]
nums = [3,2,4]
#nums = [] What if the Input is an Empty Array or an array with a Null value
target = 6
#target = 9

# Infinite Monkey approach using Pointers
def twoSum(arr, sum):
    # Edge Case
    if (arr==None):
        pass

    left = 0
    right = len(arr) -1

    while (left < right):
        if (arr[left] + arr[right]) == sum:                        
            return [left, right]
        else:            
            right = right - 1
            left = left + 1                                    
            

print(twoSum(nums, target))