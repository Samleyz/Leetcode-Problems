class Solution(object):
    def accountBalanceAfterPurchase(self, purchaseAmount):
        """
        :type purchaseAmount: int
        :rtype: int
        """
        nums = [10,20,30,40,50,60,70,80,90,100]
        pc = purchaseAmount
        if purchaseAmount < 5:
            return 100
        while purchaseAmount not in nums :
            purchaseAmount+=1
            pc -=1
            if pc in nums:
                break

        if purchaseAmount in nums:
            return 100 -purchaseAmount
        else:
            return 100 -pc
