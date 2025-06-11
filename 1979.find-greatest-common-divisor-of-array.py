class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_value = min(nums)
        max_value = max(nums)
        m = max(nums)
        while max_value != 1:
            if min_value% max_value == 0 and m% max_value == 0:
                return max_value
            max_value -=1

        return max_value
