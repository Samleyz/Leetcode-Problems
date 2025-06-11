class Solution(object):
    def minTimeToType(self, word):
        """
        :type word: str
        :rtype: int
        """
        letters = 'abcdefghijklmnopqrstuvwxyz'
        vol2 = 'nopqrstuvwxyzabcdefghijklm'
        loops =  min(
        abs(letters.index(word[0]) - letters.index('a')),
        abs(vol2.index(word[0]) - vol2.index('a'))
    )
        distance =0




        for i in range(len(word)-1):
            distance = abs(letters.index(word[i]) - letters.index(word[i+1]))
    

            if distance > len(letters) //2:
                distance = abs(vol2.index(word[i]) - vol2.index(word[i+1]))
                loops+=distance
                
            else:
                loops+=distance
                



        return loops + len(word)


