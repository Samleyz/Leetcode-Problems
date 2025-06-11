from collections import Counter
class Solution(object):
    def findLHS(self, nums):
        count = Counter(nums)
        big = 0
        curr = 0
        keys = sorted(count.keys())
        for i in range(len(keys)-1):
            if abs(keys[i] - keys[i+1]) == 1:
                curr = count[keys[i]] + count[keys[i+1]]
            big = max(big,curr)


        return big
