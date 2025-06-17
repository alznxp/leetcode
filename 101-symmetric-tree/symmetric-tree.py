# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSame(self, leftRoot, rightRoot):
        if leftRoot == None and rightRoot == None:
            return True
        if leftRoot == None or rightRoot == None:
            return False
        if leftRoot.val != rightRoot.val:
            return False
        
        return self.isSame(leftRoot.left, rightRoot.right) and self.isSame(leftRoot.right, rightRoot.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root: 
            return true

        return self.isSame(root.left, root.right)