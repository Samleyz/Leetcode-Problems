class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zeros = nums.count(0)
        ones = nums.count(1)
        

        for i in range(len(nums)):
            if i < zeros:
                nums.pop(i)
                nums.insert(i,0)
            elif zeros <= i< ones+zeros:
                nums.pop(i)
                nums.insert(i,1)

            elif ones+zeros <= i :
                nums.pop(i)
                nums.insert(i,2)
