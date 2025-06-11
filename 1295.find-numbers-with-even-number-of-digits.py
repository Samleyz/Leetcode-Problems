class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        even = 0
        for i in nums:
            if len(str(i)) % 2 ==0:
                even +=1
        return even
