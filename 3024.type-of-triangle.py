class Solution(object):
    def triangleType(self, nums):
        a = (nums[0]+nums[1])
        b= (nums[1] +nums[2])
        c = (nums[0] + nums[2])
        if a <= nums[2] or b <= nums[0] or c <= nums[1]:
            return 'none'

        seen = set()
        for i in nums:
            if i not in seen:
                seen.add(i)
    
        if len(seen) == 3:
            return 'scalene'
        elif len(seen) == 2:
            return 'isosceles'
        else:
            return 'equilateral'
