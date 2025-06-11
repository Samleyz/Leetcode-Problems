class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        s = bin(n)
        b = s[::-1]
        a = b.replace('b0','')
        print(a)
        if len(a) != 32:
            a+=(32-len(a))*'0'
        return int(a,2)
