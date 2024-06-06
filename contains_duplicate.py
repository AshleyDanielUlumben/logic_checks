# Contains Duplicate

def contDup(nums):
    # Hashset 
    hashlis = set()

    for n in range(0,len(nums)):
        if nums[n] in hashlis:
            return True
        else:
            hashlis.add(nums[n])
    return False

duplis = [1,2,3,1,5]
notdup = [1,2]
print(contDup(duplis))
print(contDup(notdup))
