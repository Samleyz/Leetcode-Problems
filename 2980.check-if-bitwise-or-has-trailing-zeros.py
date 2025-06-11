class Solution(object):
    def hasTrailingZeros(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        evens = []

        for i in nums:
            if i % 2 == 0:
                evens.append(i)
            if len(evens) == 2:
                return True
        return False
