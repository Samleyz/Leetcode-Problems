class Solution(object):
    def mySqrt(self, x):
        left=0
        right = x

        while right >= left:
            mid = (right + left) // 2
            if mid *mid<x:
                left = mid+1
            elif mid *mid>x:
                right =mid-1
            else:
                return mid
        return right
