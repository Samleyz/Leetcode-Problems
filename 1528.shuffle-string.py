class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        d=zip(indices,s)
        a=sorted(d)
        result="".join(chr for index,chr in a)
        return result
