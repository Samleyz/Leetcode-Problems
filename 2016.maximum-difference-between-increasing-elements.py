class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        maxdiff = 0
        flag = False
        for i in range(len(nums)-1):
            for j in range(i,len(nums)):
                if i < j and nums[i] < nums[j]:
                    res = nums[j] - nums[i]
                    if maxdiff < res:
                        flag = True
                        maxdiff = res
        return maxdiff if flag is True else -1
