#
# @lc app=leetcode id=1372 lang=python3
#
# [1372] Longest ZigZag Path in a Binary Tree
#

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def dfs(root: Optional[TreeNode], left: int, right: int):
            if not root:
                return
                
            nonlocal max_zz
            max_zz = max(max_zz, left, right)
            
            dfs(root.left, right + 1, 0)
            dfs(root.right, 0, left + 1)
        
        max_zz = 0
        
        dfs(root, 0, 0)
        
        return max_zz
# @lc code=end

