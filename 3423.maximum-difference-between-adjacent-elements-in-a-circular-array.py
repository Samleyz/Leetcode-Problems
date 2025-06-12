class Solution(object):
    def maxAdjacentDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = abs(nums[0]-nums[-1])

        for i in range(len(nums)-1):
            if abs(nums[i]-nums[i+1]) > m:
                m = abs(nums[i]-nums[i+1])
        return m
