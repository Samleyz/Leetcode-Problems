class Solution(object):
    def answerString(self, word, numFriends):
        """
        :type word: str
        :type numFriends: int
        :rtype: str
        """
        split = len(word) - numFriends +1


        res = ''
        if len(word) == numFriends:
            return chr((max(ord(i) for i in word)))
        if numFriends == 1:
            return word

        for i in range(0,len(word)):
            new_str = word[i:split + i]
            if new_str > res:
                res = new_str
        return res
