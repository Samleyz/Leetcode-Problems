class Solution(object):
    def plusOne(self, digits):
        listToStr = ''.join([str(elem) for elem in digits])
        l = int(listToStr)+1
        p = []
        for i in str(l): p.append(int(i))
        return p
