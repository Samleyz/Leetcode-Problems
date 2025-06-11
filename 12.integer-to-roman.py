class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        num = str(num)
        thousands = {'1':'M','2':'MM','3':'MMM'}
        hundreds = {'0':'','1':'C','2':'CC','3':'CCC','4':'CD','5':'D','6':'DC','7':'DCC','8':'DCCC','9':'CM'}
        tens = {'0':'','1':'X','2':'XX','3':'XXX','4':'XL','5':'L','6':'LX','7':'LXX','8':'LXXX','9':'XC'}
        ones = {'0':'','1':'I','2':'II','3':'III','4':'IV','5':'V','6':'VI','7':'VII','8':'VIII','9':'IX'}
        result = ''
        if len(num) == 4:
            result = thousands[num[0]]+hundreds[num[1]]+tens[num[2]]+ones[num[3]]
        if len(num) == 3:
            result = hundreds[num[0]]+tens[num[1]]+ones[num[2]]
        if len(num) == 2:
            result = tens[num[0]]+ones[num[1]]
        if len(num) == 1:
            result = ones[num[0]]

        return result
