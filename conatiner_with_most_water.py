# Conatiner with Most water

lis = [1,8,6,2,5,4,8,3,7]
# expected res -> 49
lis1 = [1,1]
# expected res -> 1

def mostWater(height):
    # Working with the two pointer approach
    # we want max area
    # Hence we pick the two extreme ends to begin with    
    # Work our way inwards

    l = 0
    r = len(height) - 1
    res = 0   

    while l <= r:            
        # length -> minimum of the right or left height
        # width -> distance from the left to right height bar 
        area = min(height[l], height[r]) * (r - l)
        res = max(area, res)
        if height[l] < height[r]:            
            l +=1
        else:
            r -= 1
    return res

print("The maxArea of the container is",mostWater(lis1))