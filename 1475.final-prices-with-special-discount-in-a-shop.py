class Solution(object):
    def finalPrices(self, prices):
        n = len(prices)
        answer = prices 
        for i in range(n):
            for j in range(i + 1, n):
                if prices[j] <= prices[i]:
                    answer[i] -= prices[j]
                    break  
        return answer
        
