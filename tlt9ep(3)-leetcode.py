class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        stringed=str(x)
        
        if (stringed[0]=="-"):
            reversed = stringed[1::-1]
            reversed = "-" + reversed
        else:
            reversed = stringed[::-1]
            
        if (int(reversed)>2147483647) or (int(reversed)<-2147483648):
            return 0
        else:    
            return reversed
