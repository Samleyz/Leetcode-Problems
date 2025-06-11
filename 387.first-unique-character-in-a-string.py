class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = set()
        
        for i in range(len(s)):
            
            if s[i] not in s[i+1:] and s[i] not in seen:
                return i
            seen.add(s[i])
        return -1
