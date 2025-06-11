class Solution(object):
    def isPossibleToSplit(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = sorted(nums)
        for i in n:
            s = n.count(i)
            if s >2:
                return False
            
        return True
