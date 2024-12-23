#
# @lc app=leetcode id=700 lang=python3
#
# [700] Search in a Binary Search Tree
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
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if root.val == val:
            return root
        
        left = self.searchBST(root.left, val)
        right = self.searchBST(root.right, val)
        
        return left if left else right
    
# @lc code=end

