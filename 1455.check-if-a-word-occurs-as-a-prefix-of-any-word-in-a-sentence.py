class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        words = sentence.split(' ')
        for e,i in enumerate(words):
            if searchWord in i[0:len(searchWord)]:
                return e+1
        return -1
