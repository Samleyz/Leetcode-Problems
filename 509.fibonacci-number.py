class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0: 
            return 0
        sums = [0,1]
        for i in range(n-1):
            s = sums[-1] + sums[-2]# f2 = 1 , f3 = 1+1 = 2
            sums.append(s)
        
        return sums[-1]
