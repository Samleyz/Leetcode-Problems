class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        biggest = 0
        curr = 0

        right = 0
        left = len(height) - 1
        n = len(height)-1
        for i in range(len(height)):
            curr = min(height[right],height[left])*n
            if curr > biggest:
                biggest = curr
            if height[right] > height[left]:
                left -=1
            else:
                right+=1
            n -=1
        return biggest
