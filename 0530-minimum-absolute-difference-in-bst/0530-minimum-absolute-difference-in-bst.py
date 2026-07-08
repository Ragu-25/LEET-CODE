# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.ans=float('inf')
        self.prev=None
        def inorder(root):
            if root is None:
                return
            inorder(root.left)
            if self.prev is not None:
                self.ans=min(self.ans,root.val-self.prev)
            self.prev=root.val
            inorder(root.right)
        inorder(root)
        return self.ans                