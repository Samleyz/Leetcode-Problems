class Solution(object):
    def mergeAlternately(self, word1, word2):
        
        length = min(len(word1), len(word2))
        if len(word1) > len(word2):
            large = word1
        else:
            large = word2

        output = ""
        for i in range(length):
            output += (word1[i] + word2[i])
        output += large[length:]

        return output
