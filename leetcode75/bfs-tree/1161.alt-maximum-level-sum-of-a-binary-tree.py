#
# @lc app=leetcode id=1161 lang=python3
#
# [1161] Maximum Level Sum of a Binary Tree
#

from collections import deque
from math import inf
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_sum = -inf
        level = 0
        level_max_sum = 0

        queue = deque([root])

        while queue:
            level += 1
            curr_level_sum = sum([el.val for el in queue])
            if curr_level_sum > max_sum:
                max_sum = curr_level_sum
                level_max_sum = level

            for _ in range(len(queue)):
                node = queue.popleft()

                for child in [node.left, node.right]:
                    if child:
                        queue.append(child)

        return level_max_sum


# @lc code=end
