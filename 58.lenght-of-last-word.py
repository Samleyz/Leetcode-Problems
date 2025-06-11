class Solution(object):
    def lengthOfLastWord(self, s):
        l = ''
        s = s.rstrip()
        rs = s[::-1]
        for i in rs:
            if i == ' ':
                break
            else:
                l += i
        return len(l)
