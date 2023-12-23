#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        smaller_value = min(p.val, q.val)
        larger_value = max(p.val, q.val)
        
        while True:
            if root.val > larger_value:
                root = root.left
            elif root.val < smaller_value:
                root = root.right
            else:
                return root
# @lc code=end

