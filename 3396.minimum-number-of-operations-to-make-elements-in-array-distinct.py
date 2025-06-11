class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = 0
        i = 0
        while True:
            if len(set(nums)) != len(nums):
                if len(nums)<= 3:
                    return counter+1
                nums.pop(i)
                nums.pop(i)
                nums.pop(i)
                counter +=1
                print(nums)
            else:
                return counter
