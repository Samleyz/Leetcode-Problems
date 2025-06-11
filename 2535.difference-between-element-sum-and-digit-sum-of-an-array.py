class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        y = 0
        x = sum(nums)
        l = [str(i) for i in nums]
        s = ''.join(l)
        for i in s:
            y+= int(i)
        return abs(x-y)
