class Solution(object):
    def maxProfit(self, prices):

        localMax = 0
        globalMin = prices[0]
        maxMax=0
       
        for i in prices:
            if i <globalMin:
                globalMin = i
                localMax = i
            elif i > localMax:
                localMax = i
                maxMax = max(localMax - globalMin,maxMax)

        return maxMax
