class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        allcaps = word.upper()
        nocaps = word.lower()
        onecap = word[0].capitalize()+word[1:].lower()
        if word == allcaps:
            return True
        elif word == nocaps:
            return True
        elif word == onecap:
            return True
        return False
