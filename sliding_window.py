# Sliding Window 

someArr = [10,3,14,6,222,45,1,0,19]

def slidingWindow(arr):
    l, r = 0, len(arr) - 1 
    while l < r:
        print(arr[l],arr[r])
        l += 1
        r -= 1

print(slidingWindow(someArr))