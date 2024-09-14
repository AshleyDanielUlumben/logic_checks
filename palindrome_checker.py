# Palindrome Checker

tstr = "saippuakivikauppias"
fstr = "malayralam"

def plaindromeCheck(somestr):

    l = 0 
    r = len(somestr) - 1
    while l < r:
        if somestr[l] == somestr[r]:            
            l +=1
            r -=1            
        else:
            return False      
    return True        

print(plaindromeCheck(fstr))

