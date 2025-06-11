class Solution(object):
    def climbStairs(self, n):
        p =1
        c = 2
        if n == 1 :
            return 1

        if n == 2:
            return 2
        else:
            for i in range(3,n+1):
                p,c = c,p+c
            return c
