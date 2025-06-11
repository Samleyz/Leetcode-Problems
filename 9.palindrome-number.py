class Solution(object):
    def isPalindrome(self, x):
        x= str(x)
        for i in x:
            if x== x[::-1]:
                return True
                break
            else:
                return False
                break
