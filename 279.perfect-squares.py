import math
class Solution:
    def numSquares(self, n: int) -> int:
        ps = [i ** 2 for i in range(1,math.isqrt(n)+1)]
        if math.isqrt(n) ** 2 == n:
            return 1
    
        if n/2 in ps :
            return 2
        if n/3 in ps:
            return 3

        for i in range(-1,len(ps)*-1,-1):
            for j in range(i,len(ps)*-1-1,-1):
                if ps[i] + ps[j] == n:
                    return 2
        for i in range(len(ps)):
            for j in range(i, len(ps)):
                for k in range(j, len(ps)):
                    if ps[i] + ps[j] + ps[k] == n:
                        return 3
        return 4
