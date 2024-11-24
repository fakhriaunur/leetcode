#
# @lc app=leetcode id=1448 lang=python3
#
# [1448] Count Good Nodes in Binary Tree
#

from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: None|TreeNode = left
        self.right: None|TreeNode = right
# @lc code=start
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root: TreeNode, max_val: float|int):
            if not root:
                return
                
            nonlocal count_good_nodes
            
            if root.val >= max_val:
                count_good_nodes += 1
                max_val = root.val
            
            dfs(root.left, max_val)
            dfs(root.right, max_val)
        
        count_good_nodes = 0
        dfs(root, float("-inf"))
        
        return count_good_nodes
# @lc code=end

