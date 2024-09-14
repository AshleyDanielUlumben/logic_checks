# Climbing Stairs

# n = 3
# 1 + 1 + 1
# 1 + 2
# 2 + 1

def countingSteps(n):

    prev, current = 1, 1

    for i in range( n - 1):
        temp = prev
        prev = prev + current
        current = prev

    return prev

print(countingSteps(4))