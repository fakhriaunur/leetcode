#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def height(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            
            left = height(node.left)
            right = height(node.right)
            
            nonlocal longest_diameter
            longest_diameter = max(longest_diameter, left + right)
            
            return 1 + max(left, right)
        
        longest_diameter = 0
        
        height(root)
        
        return longest_diameter
# @lc code=end

