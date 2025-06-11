class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        result = 0
        if flowerbed == [0] and n == 1:
            return True
        if n == 0 :
            return True
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            result += 1
        if len(flowerbed) >=4:    
            if flowerbed[-1] == 0 and flowerbed[-2] == 0:
                result += 1
        
        
        i = 1
      
        while i < len(flowerbed)-3:
            if flowerbed[i] == 0 and flowerbed[i+1] == 0 and flowerbed[i+2] ==0:
                result+=1
                i+=2
            else:
                i+=1
        if len(flowerbed) == 3:
            if flowerbed[-1] == 0 and flowerbed[-2] == 0:
                result +=1
        if result >= n:
            return True
        return False
