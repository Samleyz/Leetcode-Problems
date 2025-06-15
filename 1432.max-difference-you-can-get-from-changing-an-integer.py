class Solution:
    def maxDiff(self, num: int) -> int:
        num = str(num)
        a = None
        for i in num:

            if i != '9':
                a = num.replace(i,'9')
                break
        if a == None:
            a = num


        b = None
       
        flag = False
        for n,i in enumerate(num):
            
            if i != '1' and n == 0:
                b = num.replace(i,'1')
                break
            if i == '1' and n == 0:
                flag = True
                continue
            if i == '0':
                continue
            else:
                if i == '1' and flag == True:
                    continue
                else:
                    b = num.replace(i,'0')
                    break
        if b == None:
            b = num
        


        return abs(int(a)-int(b))
