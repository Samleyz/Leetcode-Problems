class Solution(object):
    def minSum(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        sumnum1 = sum(nums1)
        sumnum2 = sum(nums2)
    
        if sumnum1+nums1.count(0) > sumnum2 and nums2.count(0) == 0:
            return -1
        if sumnum2 + nums2.count(0) > sumnum1 and nums1.count(0) == 0:
            return -1
        if nums2.count(0) == 0 and nums1.count(0) == 0:
            return sumnum1

        nums1_val = sumnum1 + nums1.count(0)
        nums2_val = sumnum2 + nums2.count(0)

        max_val = max(nums1_val,nums2_val)

        return max_val
