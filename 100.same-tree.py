class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
     


    # Base case 1: both trees are empty, they are the same
        if not p and not q:
            return True
        
        # Base case 2: one tree is empty, the other is not, they are not the same
        if not p or not q:
            return False
        
        # Base case 3: compare the values of the nodes
        if p.val != q.val:
            return False
        
        # Recursively check the left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
