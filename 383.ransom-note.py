class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        return False if any(i for i in ransomNote if i not in magazine or ransomNote.count(i) > magazine.count(i)) else True
