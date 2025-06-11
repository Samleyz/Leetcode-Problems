class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left,right = 0, len(nums)-1
        if nums == [] or target not in nums:
            return [-1,-1]
        while True:
            if nums[left] == target and nums[right] == target:
                return [left,right]
            
            if nums[left] == target and nums[right] != target:
                right -=1
            elif nums[left] != target and nums[right] == target:
                left +=1
            else:
                right -=1
                left +=1
