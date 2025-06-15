class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if children > money:
            return -1
        money = money - children
        if money < 7:
            return 0

        childs = [1 for i in range(children)]

        for i in range(children):
            if money < 7:
                childs[i] += money
                break
            else:
                if i == children-1:
                    childs[i]+= money
                    break
                childs[i] += 7
                money -=7
    
        if 4 == childs[-1]:
            return childs.count(8)-1
        return childs.count(8)
