class Solution(object):
    def findMaxAverage(self, nums, k):
            
        # Step 1: Create the prefix sum array
        n = len(nums)
        prefix_sum = [0] * (n + 1)

        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]

        # Step 2: Find the maximum sum for subarrays of length k
        max_sum = float('-inf')
        
        for i in range(n - k + 1):
            # Calculate the sum of the subarray nums[i:i+k]
            current_sum = prefix_sum[i + k] - prefix_sum[i]
            max_sum = max(max_sum, current_sum)

        v = float("{:.5f}".format(k))
        return round(max_sum / v, 5)




