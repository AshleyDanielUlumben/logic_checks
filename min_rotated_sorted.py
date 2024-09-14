# Minimum in rotated sorted array
# Using something similar to Binary Search tree solution 
# l, r, and m pointers
# Finding the pivot of the array -> m is the pivot
# the algorithm must confine to O(log n) time.

lis = [3,4,5,1,2]
# expected res = 1

lis1 = [4,5,6,7,0,1,2]
# expected res = 0

lis2 = [1]

def minRotSort(nums):
    res = nums[0] # Initially setting the res to the left most element

    l = 0 # start pointer
    r = len(nums) - 1 # end pointer    
    

    while l <= r:      
        if nums[l] < nums[r]:
            res = min(nums[l],res)
            break

        m = (l + r) // 2 # mid pointer used a pivot
        res = min(nums[m], res)

        if nums[m] >= nums[l]: # we'll search the right portion 
            l = m + 1                    
        else:
            r = m - 1        
    return res

print("The result is :",minRotSort(lis1))    