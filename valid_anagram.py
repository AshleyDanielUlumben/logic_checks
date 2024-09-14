# Valid Anagram
s = "anagram"
t = "nagaram"

# Maybe hashmap
countT = set(t)

def validAnagram(str1, str2):        
    count = 0
    
    if len(str1) != len(str2):
        return False

    for c in str1:
        if c in countT:
            count +=1
    return count

print(validAnagram(s,t))