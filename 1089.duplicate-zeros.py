class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        i = 0
        while i!= n:

            if arr[i] == 0:
                arr.insert(i,0)
                i+=1
            i+=1
            if i > n:
                break
        while len(arr) != n:
            arr.pop(-1)
        
