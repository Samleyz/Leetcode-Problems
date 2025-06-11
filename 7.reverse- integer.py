class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= -2**31 or x >= (2**31) -1:
            return 0
        c = list(str(x))
        if x < 0:
            c.remove('-')
            c.reverse()
            r = int('-'+''.join(c))
            if r <= -2**31 or r >= (2**31) -1:
                return 0
            else: return r
        c.reverse()
        a = int(''.join(c))
        if a <= -2**31 or a >= (2**31) -1:
            return 0
        return a
