# Count all 1 bits
res = []

def decBin(nums):

    while (nums >= 1):        
        temp1 = nums % 2
        res.append(temp1)
        nums = nums // 2
    
    result = []
    for n in range(len(res)-1, -1 , -1):
        result.append(res[n])

    count = 0
    l, r = 0, len(result) - 1
    while l <= r:
        if (result[l]==1):
            count +=1
            l +=1
        else:
            l +=1        

    return result, count

n = 2147483645
print(decBin(n))