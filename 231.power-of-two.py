class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        x= 0
        while 2**x != n:
            if 2**x > n:
                return False
            else:
                x+=1
        return True
