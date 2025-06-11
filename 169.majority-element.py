class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numsdict = {}
        for i in nums:
            if i not in numsdict:
                numsdict[i] =1
            else:
                numsdict[i] += 1
        max_key = max(numsdict, key=numsdict.get)
        return max_key
