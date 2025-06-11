import math
class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        d = []
        sheet = []
        a = 1
        result = 0
        for i in dominoes:
            d.append(sorted(i))


        dominoes = d



        while any(dominoes.count(i) > 1 for i in dominoes): 

            for i in dominoes:
                a = dominoes.count(i)
               
                if a == 1:
                    continue
                sheet.append(a)
                for j in range(a):
                    dominoes.remove(i)
        


        k = 2
    
        for num in sheet:

            result += math.factorial(num) // (math.factorial(k) * math.factorial(num - k))

        return result


