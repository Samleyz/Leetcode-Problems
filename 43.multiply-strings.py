class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        result = 0
        result2 = 0
        for i in num1:
            result = result * 10 + (ord(i)-ord('0'))
           
        for j in num2:
            result2 = result2*10 + (ord(j) - ord('0'))
        
        return str(result*result2)
