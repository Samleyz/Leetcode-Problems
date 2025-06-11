class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        total = (abs(dividend) / abs(divisor))
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        

        if '-' in str(dividend) and '-' in str(divisor):
            return int(total)
        if '-' in str(dividend) or '-' in str(divisor):
            return int((total) * -1)
        else:
            return int(total)
