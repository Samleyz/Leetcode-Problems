from fractions import gcd
class Solution(object):

    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        
          
        if len(deck) < 2:
            return False

        freq = {}
        for card in deck:
            freq[card] = freq.get(card, 0) + 1

        counts = list(freq.values())
        common = counts[0]
        for c in counts[1:]:
            common = gcd(common, c)

        return common >= 2
