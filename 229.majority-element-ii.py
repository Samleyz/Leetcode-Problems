class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dict = {}

        for i in nums:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] +=1

        return [i for i,x in dict.items() if x > (len(nums)//3)]
