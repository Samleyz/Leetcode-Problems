class Solution(object):
    def removeDuplicates(self, nums):
        a = []
        for i in nums:
            if i not in a:
                a.append(i)
            else:
                continue

        for i in range(len(a)):
            nums[i] = a[i]
        while len(nums) > len(a):
            nums.pop()
        return len(a)
