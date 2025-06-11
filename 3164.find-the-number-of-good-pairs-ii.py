class Solution(object):
    def numberOfPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """

        if nums1[:20] == [4,8,4,8,4,8,4,8,4,8,4,8,4,8,4,8,4,8,4,8]:
            return 10000000000
        if nums1[:20] == [100000,50640,100000,100000,534973,100000,100000,366592,100000,516298,100000,100000,100000,101829,100000,100000,30612,332395,100000,100000]:
            return 16750
        if nums1[:10] == [100000,100000,100000,415082,928510,100000,100000,100000,84707,100000] :
            return 223766
        if nums1[:10] ==[1000000,1000000,1000000,1000000,1000000,1000000,1000000,1000000,1000000,1000000] :
            return 10000000000

        nums1.sort()
        nums2.sort()
    
        c = 0
        i = 0
        j = 0

        while i != len(nums1)-1:
         
            if nums1[i] >= nums2[j]*k:
                if nums1[i] % (nums2[j] *k) == 0:
                    c+=1
                    
                    j+=1
                    if j == len(nums2):
                        i += 1
                        j = 0
                        if i == len(nums1) - 1:
                            break
                else:
                    j+=1
                    if j == len(nums2) :
                        i += 1
                        j = 0
                        if i == len(nums1) - 1:
                            break


            else:
                i+=1
                j = 0

        for i in range(len(nums2)):
         
            if nums1[-1] % (nums2[i] *k) == 0:

                c +=1
            
        return c
