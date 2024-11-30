#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#

from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: Optional[TreeNode] = left
        self.right: Optional[TreeNode] = right


# @lc code=start
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        right_side_view = []

        queue: deque[Optional[TreeNode]] = deque([root])

        while queue:
            right_side_view.append(queue[-1].val)

            for _ in range(len(queue)):
                node = queue.popleft()

                for child in [node.left, node.right]:
                    if child:
                        queue.append(child)

        return right_side_view


# @lc code=end
