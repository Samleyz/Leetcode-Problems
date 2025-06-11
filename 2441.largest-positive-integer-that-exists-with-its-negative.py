class Solution(object):
    def findMaxK(self, nums):
        l = []
        for i in nums:
            if i and i*(-1) in nums:
                l.append(i)
        if len(l) ==0:
            return -1
        return max(l)
        
