class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        s = s+'.'
        longest = 0
        i = 0
        seen =set()
        a = 1

        while i != len(s)-1:
            if s[i] not in seen:
                seen.add(s[i])
                i+=1
                if longest < len(seen):
                    longest = len(seen)
                    print(seen)
            if s[i] in seen:
                seen.remove(s[i])
                if longest < len(seen):
                    longest = len(seen)
                    print(seen)
                seen = set()
                i = a
                a +=1
            


        return longest
