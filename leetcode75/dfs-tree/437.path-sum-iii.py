#
# @lc app=leetcode id=437 lang=python3
#
# [437] Path Sum III
#

from collections import Counter
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        path_counts = Counter({0: 1})
        def dfs(root: Optional[TreeNode], curr_sum: int) -> int:
            if not root:
                return 0
            
            nonlocal path_counts
            
            curr_sum += root.val
            
            path_count = path_counts[curr_sum - targetSum]
            
            path_counts[curr_sum] += 1
            
            path_count += dfs(root.left, curr_sum)
            path_count += dfs(root.right, curr_sum)
            path_counts[curr_sum] -= 1
            
            return path_count
        
        return dfs(root, 0)
            
# @lc code=end

