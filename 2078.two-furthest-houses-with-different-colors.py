class Solution(object):
    def maxDistance(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        left = 0
        right = len(colors) - 1
        while colors[left] == colors[right]:
            right = right - 1
        l = abs((left - right))

        left = 0
        right = len(colors) -1
        while colors[left] == colors[right]:
            left += 1
        p = abs(left - right)

        return max(l,p)
