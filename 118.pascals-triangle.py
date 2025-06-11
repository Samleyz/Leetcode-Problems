import math
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        

        res = [[1]]
        triangle = []
        num = 0
        for i in range(1,numRows):
            if i == len(triangle):
                res.append(triangle)
            else:
                for j in range(i+1):
                    triangle.append(int(math.factorial(i)/(math.factorial(i-j)*math.factorial(j))))
            res.append(triangle)
            triangle = []
        return res
