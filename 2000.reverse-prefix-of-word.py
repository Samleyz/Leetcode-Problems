class Solution(object):
    def reversePrefix(self, word, ch):
        i = word.find(ch)
        s = word[:i + 1]
        temp = ""
        if i + 1 < len(word):
            temp = word[i + 1:]
        s = s[::-1]
        return s + temp
