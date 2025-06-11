class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        numbermap = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        if len(digits) == 1:
            return list(numbermap[digits])
        result = []
        if len(digits) == 2:
            digits = list(digits)
            for char in numbermap[digits[0]]:
                for char2 in numbermap[digits[1]]:
                    result.append(char+char2)
        if len(digits) ==3:
            digits = list(digits)
            for i in numbermap[digits[0]]:
                for j in numbermap[digits[1]]:
                    for k in numbermap[digits[2]]:
                        result.append(i+j+k)
        if len(digits) == 4:
            digits = list(digits)
            for i in numbermap[digits[0]]:
                for j in numbermap[digits[1]]:
                    for k in numbermap[digits[2]]:
                        for l in numbermap[digits[3]]:
                            result.append(i+j+k+l)
        return result
