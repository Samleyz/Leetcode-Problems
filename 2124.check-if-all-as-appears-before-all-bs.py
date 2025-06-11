class Solution(object):
    def checkString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        seen = set()
        for i in s:
            seen.add(i)
            if i == 'a' and 'b' in seen:
                return False
        return True
