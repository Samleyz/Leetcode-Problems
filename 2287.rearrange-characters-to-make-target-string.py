from collections import Counter
class Solution(object):
    def rearrangeCharacters(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: int
        """
        countList = Counter(s)

        countTarget = Counter(target)

        res = 1000000
        for k,v in countTarget.items():
            if countList[k] != None:
                res = min(res, countList[k]//v)
        return res
