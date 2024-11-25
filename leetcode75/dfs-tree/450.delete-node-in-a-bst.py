#
# @lc app=leetcode id=450 lang=python3
#
# [450] Delete Node in a BST
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
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
            return root
        
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
            return root
        
        if not root.left:
            return root.right
        
        if not root.right:
            return root.left
        
        min_right_subtree = root.right
        while min_right_subtree.left:
            min_right_subtree = min_right_subtree.left
        
        root.val = min_right_subtree.val
        root.right = self.deleteNode(root.right, min_right_subtree.val)

        return root
            
# @lc code=end

