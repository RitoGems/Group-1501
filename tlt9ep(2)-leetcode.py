//Timmy Truong
//TLT9EP
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        first = int(a,2)
        second = int(b,2)
        sum = bin(first+second)
        return sum[2:]
