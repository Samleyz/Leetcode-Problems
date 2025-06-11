class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = []
        a =0
        for i in nums:
            if i == 1:
                a+=1
            if i == 0:
                s.append(a)
                a = 0
        s.append(a)
        return max(s)
