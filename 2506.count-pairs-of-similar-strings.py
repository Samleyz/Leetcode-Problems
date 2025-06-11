class Solution(object):
    def similarPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        i = 0
        j = 1
        final = 0
        if len(words) == 1:
            return 0
        while i!= len(words)-1:
            if all(char in words[i] for char in words[j]) and all(char in words[j] for char in words[i]):
            
                final+=1

            if j == len(words)-1:
                i+=1
                j = i


            j+=1

        return final
