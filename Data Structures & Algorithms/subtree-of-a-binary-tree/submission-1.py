# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSame(p, q):
            if not p and not q:
                return True
            
            if p and not q or q and not p:
                return False
            
            left = isSame(p.left, q.left)
            right = isSame(p.right, q.right)
            
            return p.val == q.val and left and right
        
        def traverse(node):
            if not node:
                return False
            if isSame(node, subRoot):
                return True
            
            return traverse(node.left) or traverse(node.right)
        return traverse(root)

