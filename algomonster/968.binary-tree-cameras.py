#
# @lc app=leetcode id=968 lang=python3
#
# [968] Binary Tree Cameras
#

from functools import lru_cache
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
# Definition for a binary tree node.
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        MAX = float("inf")

        @lru_cache(maxsize=None)
        def dfs(
            node: Optional[TreeNode],
        ) -> tuple[int | float, int | float, int | float]:
            if not node:
                return MAX, 0, 0

            left_a, left_b, left_c = dfs(node.left)
            right_a, right_b, right_c = dfs(node.right)

            a = min(left_a, left_b, left_c) + min(right_a, right_b, right_c) + 1
            b = min(left_a + right_b, left_b + right_a, left_a + right_a)
            c = left_b + right_b

            return a, b, c

        min_with_root, min_with_parent, _ = dfs(root)

        return int(min(min_with_root, min_with_parent))


# @lc code=end
