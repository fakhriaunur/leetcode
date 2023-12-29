#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
# @lc code=start
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode]) -> bool:
            if not node:
                return True
            
            if not dfs(node.left):
                return False
            
            nonlocal prev
            
            if node.val <= prev:
                return False
            
            prev = node.val
            
            if not dfs(node.right):
                return False
            
            return True
        
        prev = -float('inf')
        
        return dfs(root)
        
# @lc code=end

