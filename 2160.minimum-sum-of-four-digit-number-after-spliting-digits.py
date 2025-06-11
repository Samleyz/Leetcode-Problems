class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
        string = str(num)
        xs = list(string)
        s = [int(i) for i in xs]

        result = 0
        for i in range(2):
            n = str(min(s)) + str(max(s))
            s.remove(min(s))
            s.remove(max(s))
            result += int(n)
        return result
