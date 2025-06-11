class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        occurrences = set()
        for i in s:
            occurrences.add(s.count(i))
        if len(occurrences) >1:
            return False
        else:return True
