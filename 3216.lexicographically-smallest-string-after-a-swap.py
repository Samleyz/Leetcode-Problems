class Solution(object):
    def getSmallestString(self, s):
        """
        :type s: str
        :rtype: str
        """
        minvalue = s
        l = list(s)
        i= 0
        j=  1
        odd = ['0','2','4','6','8']
        even = ['1','3','5','7','9']
        while j != len(l):
            if s[i] in odd and s[j] in odd or s[i] in even and s[j] in even:
                l[i],l[j] = l[j],l[i]
                string = ''.join(l)
                
                if int(string)< int(minvalue):
                    minvalue = string
                    
            j+=1
            i+=1
            l = list(s)
        return str(minvalue)
