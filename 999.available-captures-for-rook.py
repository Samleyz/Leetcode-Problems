class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        pos = 0
        num_row = 0
        capture = 0
    
        for v,i in enumerate(board):

            if 'R' in i:
                for k,j in enumerate(i):

                    if j == 'R':
                        pos = k
                        num_row =v
                break
        flag = False
        cap = False
        found = False
        for num,i in enumerate(board):
            if num < num_row:
                for enum,j in enumerate(i):

                    if j == 'p' and enum == pos and flag is False:

                        cap = True
                        capture +=1
                        flag = True
                    if j == 'B' and enum == pos:
                        flag = True
                        if cap == True:
                            capture -=1
                        else: flag = False

            else:
                for enum,x in enumerate(i):
                    if x == 'p' and enum == pos:
                        capture +=1
                        found = True
                        break
                    if x == 'B' and enum == pos:
                        found = True
                        break
                if found is True:
                    break
        cap = False
        flag = False
        for num,i in enumerate(board[num_row]):
            if num < pos:
                if i == 'p' and flag is False:
                    capture +=1
                    cap = True
                    flag = True
                if i == 'B':
                    flag = True
                    if cap is True:
                        capture -=1
                        flag = False
                    else: flag = False
            else:
                if i == 'p':
                    capture+=1
                    break
                if i == 'B' :
                    break


        return capture
