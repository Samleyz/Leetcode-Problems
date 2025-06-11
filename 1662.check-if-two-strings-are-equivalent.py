class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        k1 =""
        k2 = ""
        for i in word1:
            k1 = k1+i

        for i in word2:
            k2 = k2+i

        if k1==k2:
            return True

        else:
            return False
