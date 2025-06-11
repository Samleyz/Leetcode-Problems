class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        wordmap = {}
        words = s.split(' ')
        checker = []

        if len(pattern) != len(words):
            return False

        for i in range(len(pattern)):
            if words[i] in wordmap.values():
                continue
            wordmap[pattern[i]] = words[i]
      
        for i in pattern:
            if i not in wordmap.keys():
                return False

        for i in words:
            if i not in wordmap.values():
                return False

        for i in pattern:
            checker.append(wordmap.get(i))
        if ''.join(checker) != ''.join(words):
            return False
        return True
