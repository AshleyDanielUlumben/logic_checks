someS = ['h','e','l','l','o']
someS1 = ['n','a','m','t','a','b'] 
someS2 = ['b','r','u','c','e']

def reverseString(s):
    # use pointers 
    l, r = 0, len(s) - 1

    # while the pointers have not crossed each other
    while l < r :
        s[l], s[r] = s[r], s[l]
        # moving the pointers
        l, r = l + 1, r - 1
    return s

print(reverseString(someS))


def reverseStringStack(s1):
    # empty stack
    someStack = []
    # for every character in the str we push it onto the stack
    for c in s1:
        someStack.append(c)
    i = 0
    # we pop from the stack and push it back to the str
    while someStack:
        s1[i] = someStack.pop()
        i += 1
    return s1

print(reverseStringStack(someS1))
# recursive call Not efficient
def reverseStringRecursive(s2):    
    def recursiveString(l,r):                                
        if l < r:
            s2[l],  s2[r] = s2[r], s2[l]
            recursiveString(l + 1, r-1)
    recursiveString(0,len(s2)-1)
    return s2
print(reverseStringRecursive(someS2))

