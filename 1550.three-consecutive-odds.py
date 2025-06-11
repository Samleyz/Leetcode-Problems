class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        counter = 0
        for i in arr:
            if i % 2 == 1:
                counter += 1
            if counter == 3:
                return True
            if i % 2 == 0:
                counter = 0

        return False
