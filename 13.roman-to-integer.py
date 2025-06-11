class Solution(object):
    def romanToInt(self, s):
        let = ['M', 'D', 'C', 'L', 'X', 'V', 'I', ' ']
        letters = {'M' : 1000, 'D' : 500, 'C' : 100, 'L' : 50, 'X' : 10, 'V' : 5, 'I' : 1}
        s = s + ' '
        sum = 0
        for i in range(len(s) - 1):
            if let.index(s[i]) <= let.index(s[i+1]):
                sum = sum + letters[s[i]]
            else:
                sum = sum - letters[s[i]]
        return sum
