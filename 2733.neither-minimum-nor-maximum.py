class Solution(object):
    def findNonMinOrMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=2:
            return -1
        for i in nums:
            if i == max(nums) or i == min(nums):
                continue
            else:
                return i
