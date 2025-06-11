class Solution(object):
    def maximizeSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        x = []
        for i in range(k):
            if not x:
                x.append(max(nums))
            else:
                x.append(x[i-1]+1)
        return sum(x)
