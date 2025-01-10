#
# @lc app=leetcode id=337 lang=python3
#
# [337] House Robber III
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
    def rob(self, root: Optional[TreeNode]) -> int:
        @lru_cache(maxsize=None)
        def dfs(node: Optional[TreeNode]) -> tuple[int, int]:
            if not node:
                return 0, 0

            left_inc, left_exc = dfs(node.left)
            right_inc, right_exc = dfs(node.right)

            curr_inc = node.val + left_exc + right_exc
            curr_exc = max(left_inc, left_exc) + max(right_inc, right_exc)

            return curr_inc, curr_exc

        return max(dfs(root))
        # ans = dfs(root)
        # max_ans = max(ans)
        # dfs.cache_clear()

        # return max_ans


# @lc code=end
