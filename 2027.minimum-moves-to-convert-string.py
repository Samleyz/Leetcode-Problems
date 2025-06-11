class Solution(object):
    def minimumMoves(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        i = 0
        while i < len(s):
            if s[i] == 'O':
                i+=1
                continue
            else:
                i+=3
                count +=1

        return count
