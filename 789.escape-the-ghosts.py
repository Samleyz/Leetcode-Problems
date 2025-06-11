class Solution(object):
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        my_steps = abs(target[0])+abs(target[1])
        ghost_steps = []
        x = 0
        y = 0
        for i in range(len(ghosts)):
            
            while ghosts[i][0] != target[0] or ghosts[i][1] != target[1]:
                if ghosts[i][0] < target[0]:
                    ghosts[i][0] +=1
                    x+=1
                if ghosts[i][0] > target[0]:
                    ghosts[i][0] -= 1
                    x+=1
                if ghosts[i][1] < target[1]:
                    ghosts[i][1] +=1
                    y+=1
                if ghosts[i][1] > target[1]:
                    ghosts[i][1] -=1
                    y+=1
                
            ghost_steps.append(x+y)
            x,y = 0,0
        
        return False if any(i for i in ghost_steps if i <= my_steps) else True
