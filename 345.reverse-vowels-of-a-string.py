class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        sr = s[::-1]
        jlist = [j for j in sr if j in vowels]
        beststringyouhaveeverseen = ''
        u = 0
        for i in s:
            if i in vowels:
                i = jlist[u]
                u+=1
                beststringyouhaveeverseen += i
            else:
                beststringyouhaveeverseen +=i


        return beststringyouhaveeverseen
