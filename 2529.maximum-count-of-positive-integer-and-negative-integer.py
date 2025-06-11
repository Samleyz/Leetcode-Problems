class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r = 0
        s = 0
        for i in nums:
            if i > 0:
                r+=1
            if i < 0:
                s+=1
        return max(r,s)
