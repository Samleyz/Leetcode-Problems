class Solution(object):
    def decodeMessage(self, key, message):
        """
        :type key: str
        :type message: str
        :rtype: str
        """
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        correct_key = ''
        mess = ''
        for i in key:
            if i == ' ':
                continue
            if i not in correct_key:
                correct_key += i
        for i in message:
            if i == ' ':
                mess+= ' '
            else:
                index = correct_key.index(i)
                mess += alphabet[index]
        return mess
