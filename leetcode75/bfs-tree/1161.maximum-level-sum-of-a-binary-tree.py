#
# @lc app=leetcode id=1161 lang=python3
#
# [1161] Maximum Level Sum of a Binary Tree
#

from collections import deque
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
        sum_per_level = {}
        level = 0

        queue = deque([root])

        while queue:
            level += 1
            print(f"qpl: {[el.val for el in queue]}")
            sum_per_level[level] = sum([el.val for el in queue])

            for _ in range(len(queue)):
                node = queue.popleft()

                for child in [node.left, node.right]:
                    if child:
                        queue.append(child)

        return max(sum_per_level.items(), key=lambda item: item[1])[0]


# @lc code=end
