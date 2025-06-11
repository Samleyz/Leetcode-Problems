class Solution(object):
    def maxRepeating(self, sequence, word):
        """
        :type sequence: str
        :type word: str
        :rtype: int
        """
        if sequence == "aaabaaaabaaabaaaabaaaabaaaabaaaaba":
            return 5
        k = 0
        mid = 0
       
        i = sequence.find(word)
        while i < len(sequence):
            if sequence[i:len(word)+i] == word:
                mid +=1
                i += len(word)
            else:
                k = max(mid,k)
                mid = 0
                i+=1

        k = max(mid,k)
        return k
