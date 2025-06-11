class Solution(object):
    def waysToSplitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)
        # Precompute prefix and suffix sums
        prefix_sum = [0] * n
        suffix_sum = [0] * n
        
        prefix_sum[0] = nums[0]
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]
        
        suffix_sum[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + nums[i]
        
        result = 0
        for i in range(n - 1):  # i must be < n - 1
            if prefix_sum[i] >= suffix_sum[i + 1]:
                result += 1
        
        return result

