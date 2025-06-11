class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        word = list(s)

        for i in range(len(s)):
            if ''.join(word) == goal:
                return True
            else:
                word.append(word[0])
                word.pop(0)
        return False
