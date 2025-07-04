class Solution(object):
    def countGoodTriplets(self, arr, a, b, c):
        """
        :type arr: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        result = []
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                for k in range(j+1,len(arr)):
                    if (
                            abs(arr[i] - arr[j]) <= a and
                            abs(arr[j] - arr[k]) <= b and
                            abs(arr[i] - arr[k]) <= c
                    ):
                        result.append((arr[i], arr[j], arr[k]))


        return len(result)
