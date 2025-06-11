class Solution(object):
    def isValid(self, s):
        opening = ['(','[','{']
        closing = [')',']','}']
        brackets = {'(':')','[':']','{':'}'}
        stack = []
        
        for i in s:
            if i in opening:
                stack.append(i)
            elif i in closing:
                if not stack:
                    return False
                last = stack.pop()
                if brackets[last] != i:

                    return False
    
        return True if len(stack) == 0 else False
