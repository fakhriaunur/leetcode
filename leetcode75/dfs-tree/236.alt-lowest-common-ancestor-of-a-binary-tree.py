#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left: None|TreeNode = None
        self.right: None|TreeNode = None

# @lc code=start
class Solution:
    def lowestCommonAncestor(self, root: None|TreeNode, p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
            
        if root in [p, q]:
            return root
        
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if left and right:
            return root
        
        return left if left else right
        
# @lc code=end

