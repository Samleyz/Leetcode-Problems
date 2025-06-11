class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) % 2 == 1:
            return False
        freq = {}
        for i in nums:
            if i in freq:
                freq[i] +=1
            else:
                freq[i] = 1


        for i in freq.values():

            if i % 2 != 0:
                return False
        return True
