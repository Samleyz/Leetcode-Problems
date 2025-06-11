class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        betnums = []
        digits = [int(d) for d in str(n)]
        while n != 1:

            p = sum([x**2 for x in digits])
        
            if p in betnums:
                return False
            betnums.append(p)
            digits = [int(d) for d in str(p)]

            if p == 1:
                break
        return True
