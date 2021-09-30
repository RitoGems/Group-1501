//Timmy Truong
//TLT9EP

class Solution(object):
    def isPalindrome(self, x):
        stringInput = str(x)
        reversed=stringInput[::-1]
        if (stringInput==reversed):
            return True
        else:
            return False
    
