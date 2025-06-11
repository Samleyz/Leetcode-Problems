class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        arr = []
        if nums == sorted(nums,reverse= True):
            return nums.sort()
        for i in range(-1,len(nums)*-1,-1):
            if nums[i] <= nums[i-1]:
                arr.append(nums[i])

            else:
                arr.insert(0,nums[i])
                copy = sorted(arr)
                for j in copy:

                    if nums[i-1] < j:
                        index = arr.index(j)

                        nums[i-1],arr[index] = arr[index],nums[i-1]
                        break
                break
       
        for i in range(len(arr)):
            nums.pop(-1)
        for i in sorted(arr):
            nums.append(i)

        return nums

