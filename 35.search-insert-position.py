class Solution(object):
    def searchInsert(self, nums, target):
        l = []
        for i in nums:
            l.append(i)
        for i in nums:
            if target in nums:
                return nums.index(target)
            if target not in nums:
                l.append(target)
                l.sort()
                return l.index(target)
        
