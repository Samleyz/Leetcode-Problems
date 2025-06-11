import math
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
       

        triangle = []

        for j in range(rowIndex+1):
            triangle.append(int(math.factorial(rowIndex)/(math.factorial(rowIndex-j)*math.factorial(j))))


        return triangle
