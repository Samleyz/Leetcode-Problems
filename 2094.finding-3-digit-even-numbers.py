class Solution(object):
    def findEvenNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits = [str(i) for i in digits]
        res = set()
        for i in range(len(digits)):
            for j in range(len(digits)):
                for k in range(len(digits)):
                    if digits[i] != '0':
                        if i != j != k and i != k:
                            res.add(digits[i]+digits[j]+digits[k])
                

        return sorted([int(i) for i in res if int(i) % 2 ==0 ])
