class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = bin(int(a, 2) + int(b, 2))
        c = ''
        for i in a[::-1]:

            if i == 'b':
                break
            c += i
        return c[::-1]
