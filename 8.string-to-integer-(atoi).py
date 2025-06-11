class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        nums = '0123456789'
        result = ''

        

        for i in s:
            if '-' in result and i not in nums:
                break
            elif i == ' ':
                if result == '':
                    continue
                else:
                    break
            elif '+' in result and i not in nums:
                break
            elif result == '' and i == '-' or i == '+':
                if len(result) != 0:
                    break
                result += i
            elif i not in nums and result != '':
                break
            elif result == '' and i not in nums:
                break
            else:
                result += i
        try:
            result = int(result)
        except ValueError:
            return 0

        if result > 2 ** 31 - 1:
            return 2 ** 31 - 1
        if result < -2 ** 31:
            return -2 ** 31

        return result
