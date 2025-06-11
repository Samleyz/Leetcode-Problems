class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        result = []
        a = "qwertyuiopQWERTYUIOP"
        b = "asdfghjklASDFGHJKL"
        c = "zxcvbnmZXCVBNM"

        a_counter = 0
        b_counter = 0
        c_counter = 0
        for i in words:
            for j in i:
                print(j)
                if j in a:
                    a_counter += 1
                elif j in b:
                    b_counter += 1
                elif j in c:
                    c_counter += 1
            if a_counter + b_counter == 0 or b_counter+c_counter == 0 or c_counter+a_counter == 0:
                result.append(i)
            a_counter = 0
            b_counter = 0
            c_counter = 0
        return result
