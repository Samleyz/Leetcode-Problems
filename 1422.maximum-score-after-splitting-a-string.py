class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        pocet = []
        celok = list(s)
        pridavok = ''
   
        for i in s :
            if len(celok) == 1:
                break
            pridavok += i
            pocet_nul = pridavok.count('0')
            celok.remove(i)
            
            final = pocet_nul + celok.count('1')
            pocet.append(final)


        return max(pocet)
