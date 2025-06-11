class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = [i for i in range(1,n+1)]
        total = sum(nums)
        prefix = 0
        for i in range(n):
            prefix+= nums[i]
            suffix = total -prefix +nums[i]
            if prefix == suffix:
                return i+1
        return -1
