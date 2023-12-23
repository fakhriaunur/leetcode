#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            
            left = height(node.left)
            right = height(node.right)
            
            if (
                left == -1
                or right == -1
                or abs(left - right) > 1
            ):
                return -1
            
            return 1 + max(left, right)
        
        return height(root) >= 0
# @lc code=end

