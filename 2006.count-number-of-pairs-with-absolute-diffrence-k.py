class Solution(object):
    def countKDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        counter = 0
        i = 0
        j = 1
        while True:

            if abs(nums[i] - nums[j]) == k:
                counter +=1
                #print(nums[i],nums[j])
            if i == len(nums) - 2:
                break

            if j == len(nums)-1:
                i+=1
                j= i
            
            j+=1

        return counter
